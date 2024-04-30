from reader import reader
from Simulator import *
from preAFD import import_module, prepareAFN, translateToCode
from typing import *
from Draw_diagrams import draw_AF


class YalexReader:
    def __init__(self, file_path:str):
        self.content:str = reader(file_path)
        self.variables: Dict[str, str] = {}
        self.actualRule:str = ''
        self.exportMachines: Dict[str, Dict[str, str]] = {}
        self.header = ''

    def analizeFile(self):
        expMachine = import_module('expression.py', {
                'symbol': ["'[^']'|'[\n \t]'"],
                'string': ['"([^"]| )+"'],
                'operators': ['\|', '\?', '\*', '\+', '\#', '\(', '\)', '\^', '-'],
                'set': ["\[([^[]])+\]"],
            })

        def expAnalyzer(message:str) -> str:
            nonlocal expMachine
            
            message = message.replace(r'\n', '\n').replace(r'\t', '\t').replace(r'\s', '\s')
            
            expAnalysis = exclusiveSim(expMachine, message)
            
            expResult = ''
            
            for message, token in expAnalysis:
                if token == 'symbol':
                    symbol = message[1:-1]
                    if symbol in '+*?[]{}()|_#\\' and symbol != '':
                        symbol = '\\' + symbol
                    expResult += symbol
                    continue
                elif token == 'string':
                    string = message[1:-1]
                    for symbol in string:
                        if symbol in '+*?[]{}()|_#\\' and symbol != '':
                            symbol = '\\' + symbol
                        expResult += symbol
                    continue
                elif token == 'operators':
                    if message in '-^':
                        raise Exception('Operator is only into Sets ', message)
                    expResult += message
                    continue
                elif token == 'set':
                    setAnalysis = exclusiveSim(expMachine, message[1:-1])
                    expResult += '['
                    for messageSet, tokenSet in setAnalysis:
                        if tokenSet == 'symbol':
                            symbol = messageSet[1:-1]
                            if symbol in '+*?[]{}()|_#\\' and symbol != '':
                                symbol = '\\' + symbol
                            expResult += symbol
                            continue
                        elif tokenSet == 'string':
                            string = messageSet[1:-1]
                            for symbol in string:
                                if symbol in '+*?[]{}()|_#\\' and symbol != '':
                                    symbol = '\\' + symbol
                                expResult += symbol
                            continue
                        elif tokenSet == 'operators':
                            if not messageSet in '-^':
                                raise Exception('Operator is only out of Sets ', message)
                            expResult += messageSet
                            continue
                        elif tokenSet ==0:
                            continue
                        
                        raise Exception('Error in Expression', message, messageSet)

                        
                    expResult+= ']'
                    continue
                
                elif token !=1:
                    if token ==0:
                        continue
                    if token in self.variables:
                        expResult+=self.variables[token]
                    continue
                
                raise Exception('Error in Expression', message, expAnalysis)
            
            return expResult
                        
        
        def decAnalyzer(message:str):
            nonlocal expMachine
            dec:List[str] = message.split('=',1)
            if len(dec) != 2:
                raise Exception(f'Error in variable declaration `{message}`')
            name:str = dec[0].replace('let','',1).strip()
            expression:str = dec[1].strip()
            
            expression = expAnalyzer(expression)
            variableMachine = prepareAFN({name:[name]})
            expMachine.combine_States(variableMachine)
            self.variables[name] = expression
        
        def tokAnalyzer(message:str):
            tokenMachine = import_module('tokens.py', {
               'definition': ['([^ \n\t]|\'[^\']\'|"[^"]+")+'],
               'token': ['\{([^{}]|\\\\\{|\\\\\})+\}']
            })
            
            message = message[1:] if message[0]=='|' else message
            
            tokAnalysis = exclusiveSim(tokenMachine, message)
            
            definition = ''
            tokenName = ''
            
            print(tokAnalysis)
            
            for message, token in tokAnalysis:
                if token == 'definition':
                    definition = expAnalyzer(message)
                    tokenName = 'print("'+message.replace('"','\"')+'")'if tokenName == '' else tokenName
                    
                elif token == 'token':
                    tokenName = message[1:-1].replace('\{', '{').replace('\}', '}')
            
            self.exportMachines[self.actualRule][tokenName] = [definition]
        
        def RLAnalyzer(message:str):
            nameRule:str = message.replace('rule', '', 1).replace("=", "").strip()
            self.actualRule = nameRule
            self.exportMachines[nameRule]= {}
            
        
        machine = import_module('machine.py', {
            'comments': ['\(\*[^()]+\*\)'],
            'declarations': ['let +[a-z]+ *= *\n*([^ \n\t]|\'[^\']\'|"[^"]+")+'],
            'tokens': ['(\| +)?([^ \n\t]|\'[^\']\'|"[^"]+")+( +\{([^{}]|\\\\\{|\\\\\})+\})?'],
            'RL': ['rule +[a-z]+ *='],
            'header':["\{([^{}]|\\\\\{|\\\\\})+\}"]
            })
        
        analysis = exclusiveSim(machine, self.content)
        
        inRules = True
        
        for message, token in analysis:
            if token == 'comments':
                continue
            elif token == 'declarations':
                self.actualRule = ''
                decAnalyzer(message)
            elif token == 'tokens':
                if self.actualRule == '':
                    raise Exception('Rules not declarated in first place.')
                tokAnalyzer(message)
            elif token == 'RL':
                RLAnalyzer(message)
            elif token == 'header':
                message = message[1:-1]
                self.header = message
                
        print(analysis)
                
        print(self.variables)
        print(self.exportMachines)
        
        
    def createScanners(self):
        if len(self.exportMachines) == 0:
            raise Exception ('No Scanner declared.')
        

        cout = 2

        code = ''

        codes = []

        for machine in self.exportMachines:
            print(self.exportMachines[machine])
            mach = prepareAFN(self.exportMachines[machine])
            code += translateToCode(mach, True, self.header)
            fileName = "./scanner/out_" + str(machine) + ".py"
            with open(fileName, 'w', encoding='utf-8') as fileW:
                fileW.write(code)
            cout += 1
            codes.append(fileName)
            draw_AF(mach, legend=machine, expression=machine, name='Machine', useNum=True)

        return codes