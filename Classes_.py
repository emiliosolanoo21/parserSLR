from typing import *
import pandas as pd
import tabulate as tb


class Node:
    def __init__(self, value: str or int, left: 'Node' or None = None, right: 'Node' or None = None,
                 id_: int or None = None) \
            -> None:
        self.value: str or int = value
        self.left: 'Node' or None = left
        self.right: 'Node' or None = right
        self.id_: int or None = id_
        self.is_nullable: bool = False
        self.first_pos: Set[int] = set()
        self.last_pos: Set[int] = set()
        self.isLeft: bool = False
        self.follow_pos: Set[str] = set()

    def getId(self) -> str:
        return str(id(self))


class FormatPointer:

    def __init__(self):
        self.stack: List[str or 'FormatPointer'] = []
        self.father: 'FormatPointer' or None = None
        self.actual: 'FormatPointer' = self

    def push(self, value):
        self.actual.stack.append(value)

    def inGroup(self) -> 'FormatPointer' or None:
        if id(self.actual) == id(self):
            new = FormatPointer()
            new.father = self
            self.actual.stack.append(new)
            self.actual = new
            return new
        else:
            self.actual = self.actual.inGroup()

    def __str__(self):
        result = "("
        for i in self.stack:
            if i is FormatPointer:
                result += i.__str__()
            else:
                result += str(i)
        return result + ")"

    def outGroup(self):
        result = self.actual.__str__()
        self.actual = self.actual.father
        self.actual.actual = self.actual
        self.actual.stack.pop()
        self.actual.stack.append(result)

    def plus(self):
        last = self.actual.stack.pop()
        self.actual.stack.append('(' + last + '.' + last + '*)')

    def interrogation(self):
        last = self.actual.stack.pop()
        self.actual.stack.append("(" + last + "|ε)")


class State:
    def __init__(self, value: str) -> None:
        self.value: str = value
        self.transitions: Dict[str or int, Set['State']] = {}
        self.isFinalState: bool = False
        self.token: Set[str] = set()
        self.numTrans: int = 0

    def add_transition(self, value: str or int, state: 'State') -> None:
        if value in self.transitions:
            self.transitions[value].add(state)
        else:
            self.transitions[value] = {state}

        self.numTrans += 1

    def combine_States(self, state: 'State') -> None:
        for transition in state.transitions:
            if transition in self.transitions:
                self.transitions[transition] = self.transitions[transition].union(state.transitions[transition])
            else:
                self.transitions[transition] = state.transitions[transition]

        if state.isFinalState:
            self.isFinalState = True

        self.token = self.token.union(state.token)

    def getId(self) -> str:
        return str(id(self))

    def getStates(self, transition_value) -> Set['State']:
        return self.transitions[transition_value] if transition_value in self.transitions else set()

    def __eq__(self, other):
        """Define la igualdad entre dos instancias de la clase."""
        if isinstance(other, State):
            return (self.value, id(self)) == (other.value, id(self))
        return False

    def __hash__(self):
        """Define el valor de hash de la instancia."""
        return hash((self.value, id(self)))

    def getEpsilonClean(self):
        states: Set['State'] = self.getStates(ord('ε'))
        not_explorer: Set['State'] = set()

        for state in states:
            not_explorer = not_explorer.union(state.getStates(ord('ε')))

        not_explorer = not_explorer - states

        while len(not_explorer) > 0:
            states = states.union(not_explorer)
            copy = not_explorer.copy()
            not_explorer = set()
            for state in copy:
                not_explorer = not_explorer.union(state.getStates(ord('ε')))
            not_explorer = not_explorer - states

        return states.union({self})

    def delState(self, state: 'State'):
        for transition in self.transitions:
            if state in self.transitions[transition]:
                self.transitions[transition].remove(state)

    def addToken(self, token: str):
        self.token.add(token)

    def getToken(self) -> str or None:
        return str(list(self.token)[0]) if len(self.token) > 0 else None

    def numberTransitions(self) -> int:
        return self.numTrans
    
    
class GrammarElement:
    def __init__(self, value, terminal=True) -> None:
        self.value = value
        self.terminal = terminal
        self.first = set()
        self.follow = set()
        self.ignored = False
        if terminal:
            self.first.add(self)
            
        self.production:Set[Production] = set()
    
    def addProd(self, pr:'Production'):
        self.production.add(pr)
        
    def calcFirst(self):
        seen = set()
        evaluating = list(self.production)
        while len(evaluating) > 0:
            pr = evaluating.pop(0)
            point = pr.obtainPoint()
            if point:
                if point == self:
                    continue
                if point.terminal:
                    self.first.add(point)
                    continue
                if point in seen:
                    continue
                seen.add(point)
                evaluating+=list(point.production)
                    
    def __eq__(self, other):
        """Define la igualdad entre dos instancias de la clase."""
        if isinstance(other, GrammarElement):
            return self.value == other.value
        return False

    def __hash__(self):
        """Define el valor de hash de la instancia."""
        return hash((self.value,))
    
    
class Production:
    def __init__(self,origin:'GrammarElement', direction: List['GrammarElement'],number:int, point:int = 0) -> None:
        self.origin = origin
        self.direction = tuple(direction)
        self.number:int = number
        self.point = point
        
    def passPoint(self, symbol:'GrammarElement'):
        if self.point < len(self.direction):
            if symbol == self.direction[self.point]:
                newProd:'Production' = Production(self.origin, self.direction, self.number, self.point+1)
                return newProd
        return None
    
    def calcFollow(self):
        actual = 0
        while actual < len(self.direction):
            pointingPos = self.direction[actual]
            pointingNext = None
            
            if actual+1 < len(self.direction):
                pointingNext = self.direction[actual+1]
            
            if not pointingPos.terminal:
                if pointingNext:
                    if pointingNext.terminal:
                        pointingPos.follow.add(pointingNext)
                    else:
                        for elem in pointingNext.first:
                            pointingPos.follow.add(elem)
                else:
                    for next in self.origin.follow:
                        pointingPos.follow.add(next)
            actual+=1

    def __lt__(self,other):
        if self.origin.value == other.origin.value:
            return len(self.direction) < len(other.direction)
        return self.origin.value < other.origin.value
    
    def clouser(self):
        clouserResult = {self}
        if self.point < len(self.direction):
            while True:
                tempCR = set()
                for pr in clouserResult:
                    symbol = pr.obtainPoint()
                    if symbol is not None and not symbol.terminal:
                        for pr2 in symbol.production:
                            if pr2 not in clouserResult:
                                tempCR.add(pr2)
                if len(tempCR) == 0:
                    break
                clouserResult = clouserResult.union(tempCR)
        return clouserResult
    
    def obtainPoint(self):
        if self.point < len(self.direction):
            return self.direction[self.point]
        else:
            return None
    
    def __str__(self) -> str:
        toPrint = [x.value for x in self.direction]
        toPrint.insert(self.point, '.')
        return f"{self.origin.value} -> {' '.join(toPrint)}"
        
        
    def __eq__(self, other):
        """Define la igualdad entre dos instancias de la clase."""
        if isinstance(other, Production):
            return self.origin == other.origin and self.direction == other.direction and self.point == other.point
        return False

    def __hash__(self):
        """Define el valor de hash de la instancia."""
        return hash((self.origin, self.direction, self.point))

class LR0_state:
    def __init__(self, items:List['Production'], number:int) -> None:
        self.items = tuple(sorted(items))
        self.number = number
        self.transitionsDict: Dict[GrammarElement,'LR0_state']= {}
        self.finalState = False
        self.nonTerminals:List[Production] = []
        self.terminals:List[Production] = []
        self.elses:List[Production] = []
        
        for item in self.items:
            if not item.obtainPoint():
                self.elses.append(item)
            elif item.obtainPoint().terminal:
                self.terminals.append(item)
            else:
               self.nonTerminals.append(item)
        
    def __str__(self) -> str:
        return str(self.number)+'\n'+'\n'.join([str(x) for x in self.items])
        
    def addTransition(self,symbol:'GrammarElement', state:'LR0_state'):
        self.transitionsDict[symbol] = state
    
    def __eq__(self, other):
        """Define la igualdad entre dos instancias de la clase."""
        if isinstance(other, LR0_state):
            return self.items == other.items
        return False

    def __hash__(self):
        """Define el valor de hash de la instancia."""
        return hash(self.items)
    
class SLRTable:
    def __init__(self, df:pd.DataFrame, tokens:Set, ignoredTokens:Set) -> None:
        self.df = df
        self.tokens = tokens
        self.ignoredTokens = ignoredTokens
        
    def obtainAction(self, state, symbol):
        return self.df.at[state, str(symbol)]
    
    def obtainGE(self, value):
        if value in self.tokens:
            if value in self.ignoredTokens:
                return 2
            return 0
        return 1
    
    def simulation(self, text:str):
        tokensContained = []
        for eachToken in text.split(' '):
            eachToken = eachToken.strip()
            if eachToken == '':
                continue
            GEs = self.obtainGE(eachToken)
            if GEs == 2:
                continue
            elif GEs == 0:
                tokensContained.append(eachToken)
            else:
                print(eachToken)
                raise Exception('Token not allowed.')
        
        tokensContained.append('$')
        stateStack = [0]
        
        while True:
            actualState = stateStack[-1]
            actualToken = tokensContained[0]
            
            action = self.obtainAction(actualState, actualToken)
            
            stackCopy = stateStack.copy()
            
            stackCopy.reverse()
            
            print(tb.tabulate({
                'stateStack': stackCopy,
                'input': tokensContained.copy(),
                'action': action
                }, headers='keys', tablefmt='psql'))
            
            if pd.isna(action):
                expected = self.df.columns[self.df.loc[actualState].notna()].tolist()
                
                print('Expected:\n')
                for eachElem in expected:
                    print(eachElem)
                raise Exception('Not accepted.')
            elif action[0] == 's':
                stateStack.append(action[1])
                tokensContained.pop(0)
            elif action[0] == 'r':
                for _ in range(action[1][1]):
                    stateStack.pop()
                actualState = stateStack[-1]
                A = action[1][0]
                newAction = self.obtainAction(actualState, A)
                if pd.isna(newAction):
                    raise Exception('Not existing transition between State and Symbol.')
                stateStack.append(newAction[1])
            elif action[0] == 'a':
                print('\033[92m', 'Accepted!', '\033[0m')
                break
                
