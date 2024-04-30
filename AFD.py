from typing import Dict, List, Set, Tuple
from Classes_ import Node, State


def make_direct_AFD(tree: Node, nodes: Dict[str or int, Node], alphaSet: Set[int], token: str = ''):
    alpha = list(alphaSet)

    states: Dict[Tuple[int or str, ...], State] = {tuple(tree.first_pos): State('q0')}
    toEvaluate: List[Tuple[int, ...]] = [tuple(tree.first_pos)]
    total_states: Dict[str, State] = dict()
    initSta: Tuple[int, ...] = tuple(tree.first_pos)
    total_states['q0'] = states[initSta]
    finalState: str = ''
    for state in nodes:
        if nodes[state].value == '#':
            finalState = state
            break
    gen = 1

    while len(toEvaluate) > 0:
        actualState: Tuple[int, ...] = toEvaluate.pop(0)

        for letter in alpha:
            nextState_st: Set[int] = set()
            for state in actualState:
                if nodes[state].value == letter:
                    nextState_st = nextState_st.union(nodes[state].follow_pos)

            if len(nextState_st) <= 0:
                continue
            nextState: Tuple[int, ...] = tuple(nextState_st)
            if nextState not in states:
                states[nextState] = State('q' + str(gen))
                total_states['q' + str(gen)] = states[nextState]
                if finalState in nextState_st:
                    states[nextState].isFinalState = True
                toEvaluate.append(nextState)
                gen += 1
            states[actualState].add_transition(letter, states[nextState])

    for state in states:
        if finalState in state:
            states[state].isFinalState = True
            states[state].token.add(token)

    return states, states[initSta], total_states
