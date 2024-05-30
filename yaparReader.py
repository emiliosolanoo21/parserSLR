from reader import reader
from Simulator import *
from preAFD import import_module
from typing import *
import graphviz
from Draw_diagrams import draw_AF
from Classes_ import GrammarElement, Production, LR0_state, SLRTable
import pickle
import pandas as pd
import tabulate as tb


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
        self.SLR = None
        self.LR0: Dict[LR0_state, LR0_state] = {}

    def analizeFile(self):
        yapar = import_module('yapar.py', {
            'comments': ['\/\*[^/]+\*\/'],
            'tokens': ['%token ([A-Z]+( [A-Z]+)*)'],
            'ignore': ['IGNORE ([A-Z]+( [A-Z]+)*)'],
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
            elif token == 'ignore':
                message = message.replace('IGNORE', '').split()
                for upperWord in message:
                    elem = GrammarElement(upperWord.strip())
                    if elem not in self.tokens:
                        raise Exception('Ignored, but not declared before.')
                    self.tokens[elem].ignored = True
            elif token == 'productions':
                message = message.split(':')
                key = GrammarElement(message[0], False)
                firstKey = key if firstKey is None else firstKey
                self.tokens[key]=key
                value = message[1][:-1].split("|")
                prs = []
                for pr in value:
                    if pr.strip() == "":
                        key.epsilon = True
                    prs.append(pr.strip())
                productions[key] = prs
        
        newInit = GrammarElement(firstKey.value+"'", False)
        final = GrammarElement('$')
        self.tokens[newInit] = newInit
        self.tokens[final] = final
        self.initialProduction = Production(newInit, [firstKey, final], number=1)
        self.productions[1] = self.initialProduction
        newInit.addProd(self.initialProduction)
        
        count = 2
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
                        print(element.value)
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
        
        self.LR0 = LR0States
        
        for eachToken in self.tokens:
            eachToken.calcFirst()
        for eachPr in self.productions.values():
            eachPr.calcFollow()
        for eachPr in self.productions.values():
            eachPr.calcFollow()
        for eachToken in self.tokens:
            print('--------------')
            print(eachToken.value)
            for f in eachToken.follow:
                print(f.value)
    
    def constructSLR(self):
        slr = pd.DataFrame(columns=[x.value for x in self.tokens.values()], index=[x.number for x in self.LR0.values()])
        
        for eachState in self.LR0:
            for symbol, nextState in eachState.transitionsDict.items():
                if symbol.terminal:                        
                    slr.loc[eachState.number, symbol.value] = ('s', nextState.number)
                else:
                    slr.loc[eachState.number, symbol.value] = ('g', nextState.number)
            for pr in eachState.terminals:
                if pr.obtainPoint().value == '$':
                    slr.loc[eachState.number, '$'] = ('a', 0)
            for pr in eachState.elses:
                for symbol in pr.origin.follow:
                    if not pd.isna(slr.loc[eachState.number, symbol.value]):
                        print(f"ERROR: Conflicto {str(slr.loc[eachState.number, symbol.value][0]).upper()}R")
                        result = input('Para salir presione cualquier boton, pero para continuar presione 0 ')
                        if result != '0':
                            exit(-1)
                    slr.loc[eachState.number, symbol.value] = ('r', (pr.origin.value, len(pr.direction)))
        
        print(tb.tabulate(slr, headers='keys', tablefmt='psql'))
        
        table = SLRTable(slr,set([x.value for x in self.tokens]), set([x.value for x in self.tokens if x.ignored]))
        
        self.SLR = table
        
        with open('table.pkl', 'wb') as file:
            pickle.dump(table, file)

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
    