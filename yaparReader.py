from reader import reader
from Simulator import *
from preAFD import import_module
from typing import *
import graphviz
from Draw_diagrams import draw_AF
from Classes_ import GrammarElement, Production, LR0_state


class YaparReader:
    def __init__(self, file_path:str):
        self.content:str = reader(file_path)
        self.variables: Dict[str, str] = {}
        self.actualRule:str = ''
        self.exportMachines: Dict[str, Dict[str, str]] = {}
        self.header = ''
        self.tokens: Dict[GrammarElement, GrammarElement] = {}
        self.keys = []
        self.productions: Dict[int, Production] = {}
        self.initialProduction: Production = None
        self.initState = None

    def analizeFile(self):
        yapar = import_module('yapar.py', {
            'comments': ['\/\*[^/]+\*\/'],
            'tokens': ['%token ([A-Z]+( [A-Z]+)*)'],
            'productions': ['[a-z]+\:(((\n|\t| )*([a-z]+|[A-Z]+| )*)((\n|\t| )*\| *((\n|\t| )*([a-z]+|[A-Z]+| )*))*)((\n|\t| )*\;)']
        })

        analysis = exclusiveSim(yapar, self.content)
        productions:Dict[GrammarElement, str] = {}
        firstKey = None
        
        for message, token in analysis:
            if token == 'comments':
                continue
            elif token == 'tokens':
                message = message.replace('%token', '').split()
                for upperWord in message:
                    elem = GrammarElement(upperWord.strip())
                    self.tokens[elem] = elem
            elif token == 'productions':
                message = message.split(':')
                key = GrammarElement(message[0], False)
                firstKey = key if firstKey is None else firstKey
                self.tokens[key]=key
                value = message[1][:-1].split("|")
                prs = []
                for pr in value:
                    prs.append(pr.strip())
                productions[key] = prs
        
        newInit = GrammarElement(firstKey.value+"'", False)
        final = GrammarElement('$')
        self.tokens[newInit] = newInit
        self.tokens[final] = final
        self.initialProduction = Production(newInit, [firstKey, final], number=1)
        self.productions[1] = self.initialProduction
        newInit.addProd(self.initialProduction)
        
        count= 2
        for key in productions:
            prs = productions[key]
            for pr in prs:
                direction = pr.split(' ')
                direction = [GrammarElement(x.strip()) for x in direction]
                real_direction = []
                for element in direction:
                    if element in self.tokens:
                        real_direction.append(self.tokens[element])
                    else:
                        raise Exception(element.value + ' not declared')
                
                
                newProd = Production(origin=key, direction=real_direction, number=count)
                self.productions[count] = newProd
                count+=1
                key.addProd(newProd)
 
        for number, pr in self.productions.items():
            print(number, '.  ', str(pr))
        
        LR0List = self.initialProduction.clouser()
        
        initLR0 = LR0_state(LR0List, 0)
        
        evalStates = [initLR0]
        
        counter = 1
        
        LR0States = {initLR0:initLR0}
        
        self.initState = initLR0
        
        while len(evalStates) > 0:
            print(len(evalStates))
            state = evalStates.pop(0)
            for GE in self.tokens:
                newState = set()
                for item in state.items:
                    newItem = item.passPoint(GE)
                    if newItem is not None:
                        NIclouser = newItem.clouser()
                        newState = newState.union(NIclouser)
                if len(newState) != 0:
                    if GE.value == '$':
                        state.finalState = True
                        continue
                    newLR0 = LR0_state(newState,counter)
                    if newLR0 in LR0States:
                        newLR0 = LR0States[newLR0]
                    else:
                        LR0States[newLR0] = newLR0
                        evalStates.append(newLR0)
                        counter+=1
                    state.addTransition(GE, newLR0)
        
    def drawLR0(self, explicit=False):
        dot = graphviz.Digraph(comment='LR0')
        dot.attr(rankdir='LR')
        statesTraveled = set()

        def drawState(state:'LR0_state'):
            nonlocal explicit
            statesTraveled.add(state)
            dot.node(str(state.number), label=str(state.number) if not explicit else str(state), shape='doublecircle' if state.finalState else 'circle')
            for transition in state.transitionsDict:
                destiny = state.transitionsDict[transition]
                if destiny not in statesTraveled:
                    drawState(destiny)
                dot.edge(str(state.number), str(destiny.number), label=transition.value)

        drawState(self.initState)
        name = 'explicit' if explicit else ''
        dot.render('LR0_'+name+'.gv', view = True, directory = './')
        
if __name__ == "__main__":
    readerYapar = YaparReader("./slr-1.yalp")
    readerYapar.analizeFile()
    readerYapar.drawLR0()
    readerYapar.drawLR0(True)