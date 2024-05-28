from typing import *


import argparse
parser = argparse.ArgumentParser(description='Simulate a machine')
parser.add_argument('source', help='Source file')

parser.add_argument('-o', help='Output file', default='a.out')
fileOut = parser.parse_args().o
with open(fileOut, 'w') as archivo:
    # Escribe datos en el archivo
    archivo.write("")

class State:
    def __init__(self, value: str) -> None:
        self.value: str = value
        self.transitions: Dict[str or int, Set['State']] = {}
        self.isFinalState: bool = False
        self.numTrans: int = 0

    def add_transition(self, value: str or int, state: 'State') -> None:
        if value in self.transitions:
            self.transitions[value].add(state)
        else:
            self.transitions[value] = {state}

        self.numTrans += 1

    def getStates(self, transition_value) -> Set['State']:
        return self.transitions[transition_value] if transition_value in self.transitions else set()

    def __eq__(self, other):
        if isinstance(other, State):
            return (self.value, id(self)) == (other.value, id(self))
        return False

    def __hash__(self):
        return hash((self.value, id(self)))

    def getToken(self) -> str or None:
        return str(list(self.token)[0]) if len(self.token) > 0 else None

    def numberTransitions(self) -> int:
        return self.numTrans
        



k1 = State('k1')
j1 = State('j1')
h1 = State('h1')
g1 = State('g1')
f1 = State('f1')
e10 = State('e10')
e9 = State('e9')
e8 = State('e8')
e7 = State('e7')
e6 = State('e6')
e5 = State('e5')
e4 = State('e4')
e3 = State('e3')
e2 = State('e2')
e1 = State('e1')
d1 = State('d1')
c10 = State('c10')
c9 = State('c9')
c8 = State('c8')
c7 = State('c7')
c6 = State('c6')
c5 = State('c5')
c4 = State('c4')
c3 = State('c3')
c2 = State('c2')
c1 = State('c1')
i2 = State('i2')
i1 = State('i1')
b1 = State('b1')
a4 = State('a4')
a3 = State('a3')
a2 = State('a2')
a1 = State('a1')
a0 = State('a0')
a0.add_transition(47, a1)
a0.add_transition(97, b1)
a0.add_transition(98, b1)
a0.add_transition(99, b1)
a0.add_transition(100, b1)
a0.add_transition(101, b1)
a0.add_transition(102, b1)
a0.add_transition(103, b1)
a0.add_transition(104, b1)
a0.add_transition(105, b1)
a0.add_transition(106, b1)
a0.add_transition(107, b1)
a0.add_transition(108, b1)
a0.add_transition(109, b1)
a0.add_transition(110, b1)
a0.add_transition(111, b1)
a0.add_transition(112, b1)
a0.add_transition(113, b1)
a0.add_transition(114, b1)
a0.add_transition(115, b1)
a0.add_transition(116, b1)
a0.add_transition(117, b1)
a0.add_transition(118, b1)
a0.add_transition(119, b1)
a0.add_transition(120, b1)
a0.add_transition(121, b1)
a0.add_transition(122, b1)
a0.add_transition(37, i1)
a0.add_transition(37, c1)
a0.add_transition(65, d1)
a0.add_transition(66, d1)
a0.add_transition(67, d1)
a0.add_transition(68, d1)
a0.add_transition(69, d1)
a0.add_transition(70, d1)
a0.add_transition(71, d1)
a0.add_transition(72, d1)
a0.add_transition(73, d1)
a0.add_transition(73, e1)
a0.add_transition(74, d1)
a0.add_transition(75, d1)
a0.add_transition(76, d1)
a0.add_transition(77, d1)
a0.add_transition(78, d1)
a0.add_transition(79, d1)
a0.add_transition(80, d1)
a0.add_transition(81, d1)
a0.add_transition(82, d1)
a0.add_transition(83, d1)
a0.add_transition(84, d1)
a0.add_transition(85, d1)
a0.add_transition(86, d1)
a0.add_transition(87, d1)
a0.add_transition(88, d1)
a0.add_transition(89, d1)
a0.add_transition(90, d1)
a0.add_transition(58, f1)
a0.add_transition(59, g1)
a0.add_transition(124, h1)
a0.add_transition(9, j1)
a0.add_transition(10, k1)

a1.add_transition(42, a2)

a2.add_transition(0, a2)
a2.add_transition(1, a2)
a2.add_transition(2, a2)
a2.add_transition(3, a2)
a2.add_transition(4, a2)
a2.add_transition(5, a2)
a2.add_transition(6, a2)
a2.add_transition(7, a2)
a2.add_transition(8, a2)
a2.add_transition(9, a2)
a2.add_transition(10, a2)
a2.add_transition(11, a2)
a2.add_transition(12, a2)
a2.add_transition(13, a2)
a2.add_transition(14, a2)
a2.add_transition(15, a2)
a2.add_transition(16, a2)
a2.add_transition(17, a2)
a2.add_transition(18, a2)
a2.add_transition(19, a2)
a2.add_transition(20, a2)
a2.add_transition(21, a2)
a2.add_transition(22, a2)
a2.add_transition(23, a2)
a2.add_transition(24, a2)
a2.add_transition(25, a2)
a2.add_transition(26, a2)
a2.add_transition(27, a2)
a2.add_transition(28, a2)
a2.add_transition(29, a2)
a2.add_transition(30, a2)
a2.add_transition(31, a2)
a2.add_transition(32, a2)
a2.add_transition(33, a2)
a2.add_transition(34, a2)
a2.add_transition(35, a2)
a2.add_transition(36, a2)
a2.add_transition(37, a2)
a2.add_transition(38, a2)
a2.add_transition(39, a2)
a2.add_transition(40, a2)
a2.add_transition(41, a2)
a2.add_transition(42, a3)
a2.add_transition(43, a2)
a2.add_transition(44, a2)
a2.add_transition(45, a2)
a2.add_transition(46, a2)
a2.add_transition(48, a2)
a2.add_transition(49, a2)
a2.add_transition(50, a2)
a2.add_transition(51, a2)
a2.add_transition(52, a2)
a2.add_transition(53, a2)
a2.add_transition(54, a2)
a2.add_transition(55, a2)
a2.add_transition(56, a2)
a2.add_transition(57, a2)
a2.add_transition(58, a2)
a2.add_transition(59, a2)
a2.add_transition(60, a2)
a2.add_transition(61, a2)
a2.add_transition(62, a2)
a2.add_transition(63, a2)
a2.add_transition(64, a2)
a2.add_transition(65, a2)
a2.add_transition(66, a2)
a2.add_transition(67, a2)
a2.add_transition(68, a2)
a2.add_transition(69, a2)
a2.add_transition(70, a2)
a2.add_transition(71, a2)
a2.add_transition(72, a2)
a2.add_transition(73, a2)
a2.add_transition(74, a2)
a2.add_transition(75, a2)
a2.add_transition(76, a2)
a2.add_transition(77, a2)
a2.add_transition(78, a2)
a2.add_transition(79, a2)
a2.add_transition(80, a2)
a2.add_transition(81, a2)
a2.add_transition(82, a2)
a2.add_transition(83, a2)
a2.add_transition(84, a2)
a2.add_transition(85, a2)
a2.add_transition(86, a2)
a2.add_transition(87, a2)
a2.add_transition(88, a2)
a2.add_transition(89, a2)
a2.add_transition(90, a2)
a2.add_transition(91, a2)
a2.add_transition(92, a2)
a2.add_transition(93, a2)
a2.add_transition(94, a2)
a2.add_transition(95, a2)
a2.add_transition(96, a2)
a2.add_transition(97, a2)
a2.add_transition(98, a2)
a2.add_transition(99, a2)
a2.add_transition(100, a2)
a2.add_transition(101, a2)
a2.add_transition(102, a2)
a2.add_transition(103, a2)
a2.add_transition(104, a2)
a2.add_transition(105, a2)
a2.add_transition(106, a2)
a2.add_transition(107, a2)
a2.add_transition(108, a2)
a2.add_transition(109, a2)
a2.add_transition(110, a2)
a2.add_transition(111, a2)
a2.add_transition(112, a2)
a2.add_transition(113, a2)
a2.add_transition(114, a2)
a2.add_transition(115, a2)
a2.add_transition(116, a2)
a2.add_transition(117, a2)
a2.add_transition(118, a2)
a2.add_transition(119, a2)
a2.add_transition(120, a2)
a2.add_transition(121, a2)
a2.add_transition(122, a2)
a2.add_transition(123, a2)
a2.add_transition(124, a2)
a2.add_transition(125, a2)
a2.add_transition(126, a2)
a2.add_transition(127, a2)
a2.add_transition(128, a2)
a2.add_transition(129, a2)
a2.add_transition(130, a2)
a2.add_transition(131, a2)
a2.add_transition(132, a2)
a2.add_transition(133, a2)
a2.add_transition(134, a2)
a2.add_transition(135, a2)
a2.add_transition(136, a2)
a2.add_transition(137, a2)
a2.add_transition(138, a2)
a2.add_transition(139, a2)
a2.add_transition(140, a2)
a2.add_transition(141, a2)
a2.add_transition(142, a2)
a2.add_transition(143, a2)
a2.add_transition(144, a2)
a2.add_transition(145, a2)
a2.add_transition(146, a2)
a2.add_transition(147, a2)
a2.add_transition(148, a2)
a2.add_transition(149, a2)
a2.add_transition(150, a2)
a2.add_transition(151, a2)
a2.add_transition(152, a2)
a2.add_transition(153, a2)
a2.add_transition(154, a2)
a2.add_transition(155, a2)
a2.add_transition(156, a2)
a2.add_transition(157, a2)
a2.add_transition(158, a2)
a2.add_transition(159, a2)
a2.add_transition(160, a2)
a2.add_transition(161, a2)
a2.add_transition(162, a2)
a2.add_transition(163, a2)
a2.add_transition(164, a2)
a2.add_transition(165, a2)
a2.add_transition(166, a2)
a2.add_transition(167, a2)
a2.add_transition(168, a2)
a2.add_transition(169, a2)
a2.add_transition(170, a2)
a2.add_transition(171, a2)
a2.add_transition(172, a2)
a2.add_transition(173, a2)
a2.add_transition(174, a2)
a2.add_transition(175, a2)
a2.add_transition(176, a2)
a2.add_transition(177, a2)
a2.add_transition(178, a2)
a2.add_transition(179, a2)
a2.add_transition(180, a2)
a2.add_transition(181, a2)
a2.add_transition(182, a2)
a2.add_transition(183, a2)
a2.add_transition(184, a2)
a2.add_transition(185, a2)
a2.add_transition(186, a2)
a2.add_transition(187, a2)
a2.add_transition(188, a2)
a2.add_transition(189, a2)
a2.add_transition(190, a2)
a2.add_transition(191, a2)
a2.add_transition(192, a2)
a2.add_transition(193, a2)
a2.add_transition(194, a2)
a2.add_transition(195, a2)
a2.add_transition(196, a2)
a2.add_transition(197, a2)
a2.add_transition(198, a2)
a2.add_transition(199, a2)
a2.add_transition(200, a2)
a2.add_transition(201, a2)
a2.add_transition(202, a2)
a2.add_transition(203, a2)
a2.add_transition(204, a2)
a2.add_transition(205, a2)
a2.add_transition(206, a2)
a2.add_transition(207, a2)
a2.add_transition(208, a2)
a2.add_transition(209, a2)
a2.add_transition(210, a2)
a2.add_transition(211, a2)
a2.add_transition(212, a2)
a2.add_transition(213, a2)
a2.add_transition(214, a2)
a2.add_transition(215, a2)
a2.add_transition(216, a2)
a2.add_transition(217, a2)
a2.add_transition(218, a2)
a2.add_transition(219, a2)
a2.add_transition(220, a2)
a2.add_transition(221, a2)
a2.add_transition(222, a2)
a2.add_transition(223, a2)
a2.add_transition(224, a2)
a2.add_transition(225, a2)
a2.add_transition(226, a2)
a2.add_transition(227, a2)
a2.add_transition(228, a2)
a2.add_transition(229, a2)
a2.add_transition(230, a2)
a2.add_transition(231, a2)
a2.add_transition(232, a2)
a2.add_transition(233, a2)
a2.add_transition(234, a2)
a2.add_transition(235, a2)
a2.add_transition(236, a2)
a2.add_transition(237, a2)
a2.add_transition(238, a2)
a2.add_transition(239, a2)
a2.add_transition(240, a2)
a2.add_transition(241, a2)
a2.add_transition(242, a2)
a2.add_transition(243, a2)
a2.add_transition(244, a2)
a2.add_transition(245, a2)
a2.add_transition(246, a2)
a2.add_transition(247, a2)
a2.add_transition(248, a2)
a2.add_transition(249, a2)
a2.add_transition(250, a2)
a2.add_transition(251, a2)
a2.add_transition(252, a2)
a2.add_transition(253, a2)
a2.add_transition(254, a2)
a2.add_transition(255, a2)

a3.add_transition(0, a2)
a3.add_transition(1, a2)
a3.add_transition(2, a2)
a3.add_transition(3, a2)
a3.add_transition(4, a2)
a3.add_transition(5, a2)
a3.add_transition(6, a2)
a3.add_transition(7, a2)
a3.add_transition(8, a2)
a3.add_transition(9, a2)
a3.add_transition(10, a2)
a3.add_transition(11, a2)
a3.add_transition(12, a2)
a3.add_transition(13, a2)
a3.add_transition(14, a2)
a3.add_transition(15, a2)
a3.add_transition(16, a2)
a3.add_transition(17, a2)
a3.add_transition(18, a2)
a3.add_transition(19, a2)
a3.add_transition(20, a2)
a3.add_transition(21, a2)
a3.add_transition(22, a2)
a3.add_transition(23, a2)
a3.add_transition(24, a2)
a3.add_transition(25, a2)
a3.add_transition(26, a2)
a3.add_transition(27, a2)
a3.add_transition(28, a2)
a3.add_transition(29, a2)
a3.add_transition(30, a2)
a3.add_transition(31, a2)
a3.add_transition(32, a2)
a3.add_transition(33, a2)
a3.add_transition(34, a2)
a3.add_transition(35, a2)
a3.add_transition(36, a2)
a3.add_transition(37, a2)
a3.add_transition(38, a2)
a3.add_transition(39, a2)
a3.add_transition(40, a2)
a3.add_transition(41, a2)
a3.add_transition(42, a3)
a3.add_transition(43, a2)
a3.add_transition(44, a2)
a3.add_transition(45, a2)
a3.add_transition(46, a2)
a3.add_transition(47, a4)
a3.add_transition(48, a2)
a3.add_transition(49, a2)
a3.add_transition(50, a2)
a3.add_transition(51, a2)
a3.add_transition(52, a2)
a3.add_transition(53, a2)
a3.add_transition(54, a2)
a3.add_transition(55, a2)
a3.add_transition(56, a2)
a3.add_transition(57, a2)
a3.add_transition(58, a2)
a3.add_transition(59, a2)
a3.add_transition(60, a2)
a3.add_transition(61, a2)
a3.add_transition(62, a2)
a3.add_transition(63, a2)
a3.add_transition(64, a2)
a3.add_transition(65, a2)
a3.add_transition(66, a2)
a3.add_transition(67, a2)
a3.add_transition(68, a2)
a3.add_transition(69, a2)
a3.add_transition(70, a2)
a3.add_transition(71, a2)
a3.add_transition(72, a2)
a3.add_transition(73, a2)
a3.add_transition(74, a2)
a3.add_transition(75, a2)
a3.add_transition(76, a2)
a3.add_transition(77, a2)
a3.add_transition(78, a2)
a3.add_transition(79, a2)
a3.add_transition(80, a2)
a3.add_transition(81, a2)
a3.add_transition(82, a2)
a3.add_transition(83, a2)
a3.add_transition(84, a2)
a3.add_transition(85, a2)
a3.add_transition(86, a2)
a3.add_transition(87, a2)
a3.add_transition(88, a2)
a3.add_transition(89, a2)
a3.add_transition(90, a2)
a3.add_transition(91, a2)
a3.add_transition(92, a2)
a3.add_transition(93, a2)
a3.add_transition(94, a2)
a3.add_transition(95, a2)
a3.add_transition(96, a2)
a3.add_transition(97, a2)
a3.add_transition(98, a2)
a3.add_transition(99, a2)
a3.add_transition(100, a2)
a3.add_transition(101, a2)
a3.add_transition(102, a2)
a3.add_transition(103, a2)
a3.add_transition(104, a2)
a3.add_transition(105, a2)
a3.add_transition(106, a2)
a3.add_transition(107, a2)
a3.add_transition(108, a2)
a3.add_transition(109, a2)
a3.add_transition(110, a2)
a3.add_transition(111, a2)
a3.add_transition(112, a2)
a3.add_transition(113, a2)
a3.add_transition(114, a2)
a3.add_transition(115, a2)
a3.add_transition(116, a2)
a3.add_transition(117, a2)
a3.add_transition(118, a2)
a3.add_transition(119, a2)
a3.add_transition(120, a2)
a3.add_transition(121, a2)
a3.add_transition(122, a2)
a3.add_transition(123, a2)
a3.add_transition(124, a2)
a3.add_transition(125, a2)
a3.add_transition(126, a2)
a3.add_transition(127, a2)
a3.add_transition(128, a2)
a3.add_transition(129, a2)
a3.add_transition(130, a2)
a3.add_transition(131, a2)
a3.add_transition(132, a2)
a3.add_transition(133, a2)
a3.add_transition(134, a2)
a3.add_transition(135, a2)
a3.add_transition(136, a2)
a3.add_transition(137, a2)
a3.add_transition(138, a2)
a3.add_transition(139, a2)
a3.add_transition(140, a2)
a3.add_transition(141, a2)
a3.add_transition(142, a2)
a3.add_transition(143, a2)
a3.add_transition(144, a2)
a3.add_transition(145, a2)
a3.add_transition(146, a2)
a3.add_transition(147, a2)
a3.add_transition(148, a2)
a3.add_transition(149, a2)
a3.add_transition(150, a2)
a3.add_transition(151, a2)
a3.add_transition(152, a2)
a3.add_transition(153, a2)
a3.add_transition(154, a2)
a3.add_transition(155, a2)
a3.add_transition(156, a2)
a3.add_transition(157, a2)
a3.add_transition(158, a2)
a3.add_transition(159, a2)
a3.add_transition(160, a2)
a3.add_transition(161, a2)
a3.add_transition(162, a2)
a3.add_transition(163, a2)
a3.add_transition(164, a2)
a3.add_transition(165, a2)
a3.add_transition(166, a2)
a3.add_transition(167, a2)
a3.add_transition(168, a2)
a3.add_transition(169, a2)
a3.add_transition(170, a2)
a3.add_transition(171, a2)
a3.add_transition(172, a2)
a3.add_transition(173, a2)
a3.add_transition(174, a2)
a3.add_transition(175, a2)
a3.add_transition(176, a2)
a3.add_transition(177, a2)
a3.add_transition(178, a2)
a3.add_transition(179, a2)
a3.add_transition(180, a2)
a3.add_transition(181, a2)
a3.add_transition(182, a2)
a3.add_transition(183, a2)
a3.add_transition(184, a2)
a3.add_transition(185, a2)
a3.add_transition(186, a2)
a3.add_transition(187, a2)
a3.add_transition(188, a2)
a3.add_transition(189, a2)
a3.add_transition(190, a2)
a3.add_transition(191, a2)
a3.add_transition(192, a2)
a3.add_transition(193, a2)
a3.add_transition(194, a2)
a3.add_transition(195, a2)
a3.add_transition(196, a2)
a3.add_transition(197, a2)
a3.add_transition(198, a2)
a3.add_transition(199, a2)
a3.add_transition(200, a2)
a3.add_transition(201, a2)
a3.add_transition(202, a2)
a3.add_transition(203, a2)
a3.add_transition(204, a2)
a3.add_transition(205, a2)
a3.add_transition(206, a2)
a3.add_transition(207, a2)
a3.add_transition(208, a2)
a3.add_transition(209, a2)
a3.add_transition(210, a2)
a3.add_transition(211, a2)
a3.add_transition(212, a2)
a3.add_transition(213, a2)
a3.add_transition(214, a2)
a3.add_transition(215, a2)
a3.add_transition(216, a2)
a3.add_transition(217, a2)
a3.add_transition(218, a2)
a3.add_transition(219, a2)
a3.add_transition(220, a2)
a3.add_transition(221, a2)
a3.add_transition(222, a2)
a3.add_transition(223, a2)
a3.add_transition(224, a2)
a3.add_transition(225, a2)
a3.add_transition(226, a2)
a3.add_transition(227, a2)
a3.add_transition(228, a2)
a3.add_transition(229, a2)
a3.add_transition(230, a2)
a3.add_transition(231, a2)
a3.add_transition(232, a2)
a3.add_transition(233, a2)
a3.add_transition(234, a2)
a3.add_transition(235, a2)
a3.add_transition(236, a2)
a3.add_transition(237, a2)
a3.add_transition(238, a2)
a3.add_transition(239, a2)
a3.add_transition(240, a2)
a3.add_transition(241, a2)
a3.add_transition(242, a2)
a3.add_transition(243, a2)
a3.add_transition(244, a2)
a3.add_transition(245, a2)
a3.add_transition(246, a2)
a3.add_transition(247, a2)
a3.add_transition(248, a2)
a3.add_transition(249, a2)
a3.add_transition(250, a2)
a3.add_transition(251, a2)
a3.add_transition(252, a2)
a3.add_transition(253, a2)
a3.add_transition(254, a2)
a3.add_transition(255, a2)

a4.isFinalState = True


def tk_a4(): 
	
	with open(fileOut, 'a') as archivo:
	    # Escribe datos en el archivo
	    archivo.write("COMMENT ")  
	


a4.token = tk_a4

b1.isFinalState = True


def tk_b1(): 
	
	with open(fileOut, 'a') as archivo:
	    # Escribe datos en el archivo
	    archivo.write("LOWERCASE ")     
	


b1.token = tk_b1
b1.add_transition(97, b1)
b1.add_transition(98, b1)
b1.add_transition(99, b1)
b1.add_transition(100, b1)
b1.add_transition(101, b1)
b1.add_transition(102, b1)
b1.add_transition(103, b1)
b1.add_transition(104, b1)
b1.add_transition(105, b1)
b1.add_transition(106, b1)
b1.add_transition(107, b1)
b1.add_transition(108, b1)
b1.add_transition(109, b1)
b1.add_transition(110, b1)
b1.add_transition(111, b1)
b1.add_transition(112, b1)
b1.add_transition(113, b1)
b1.add_transition(114, b1)
b1.add_transition(115, b1)
b1.add_transition(116, b1)
b1.add_transition(117, b1)
b1.add_transition(118, b1)
b1.add_transition(119, b1)
b1.add_transition(120, b1)
b1.add_transition(121, b1)
b1.add_transition(122, b1)

i1.add_transition(37, i2)

i2.isFinalState = True


def tk_i2(): 
	
	with open(fileOut, 'a') as archivo:
	    # Escribe datos en el archivo
	    archivo.write("SPLITTER ")
	


i2.token = tk_i2

c1.add_transition(116, c2)

c2.add_transition(111, c3)

c3.add_transition(107, c4)

c4.add_transition(101, c5)

c5.add_transition(110, c6)

c6.add_transition(32, c7)

c7.add_transition(32, c7)
c7.add_transition(65, c8)
c7.add_transition(66, c8)
c7.add_transition(67, c8)
c7.add_transition(68, c8)
c7.add_transition(69, c8)
c7.add_transition(70, c8)
c7.add_transition(71, c8)
c7.add_transition(72, c8)
c7.add_transition(73, c8)
c7.add_transition(74, c8)
c7.add_transition(75, c8)
c7.add_transition(76, c8)
c7.add_transition(77, c8)
c7.add_transition(78, c8)
c7.add_transition(79, c8)
c7.add_transition(80, c8)
c7.add_transition(81, c8)
c7.add_transition(82, c8)
c7.add_transition(83, c8)
c7.add_transition(84, c8)
c7.add_transition(85, c8)
c7.add_transition(86, c8)
c7.add_transition(87, c8)
c7.add_transition(88, c8)
c7.add_transition(89, c8)
c7.add_transition(90, c8)

c8.add_transition(32, c9)
c8.add_transition(65, c8)
c8.add_transition(66, c8)
c8.add_transition(67, c8)
c8.add_transition(68, c8)
c8.add_transition(69, c8)
c8.add_transition(70, c8)
c8.add_transition(71, c8)
c8.add_transition(72, c8)
c8.add_transition(73, c8)
c8.add_transition(74, c8)
c8.add_transition(75, c8)
c8.add_transition(76, c8)
c8.add_transition(77, c8)
c8.add_transition(78, c8)
c8.add_transition(79, c8)
c8.add_transition(80, c8)
c8.add_transition(81, c8)
c8.add_transition(82, c8)
c8.add_transition(83, c8)
c8.add_transition(84, c8)
c8.add_transition(85, c8)
c8.add_transition(86, c8)
c8.add_transition(87, c8)
c8.add_transition(88, c8)
c8.add_transition(89, c8)
c8.add_transition(90, c8)

c9.isFinalState = True


def tk_c9(): 
	
	with open(fileOut, 'a') as archivo:
	    # Escribe datos en el archivo
	    archivo.write("TOKEN ")
	


c9.token = tk_c9
c9.add_transition(32, c9)
c9.add_transition(65, c10)
c9.add_transition(66, c10)
c9.add_transition(67, c10)
c9.add_transition(68, c10)
c9.add_transition(69, c10)
c9.add_transition(70, c10)
c9.add_transition(71, c10)
c9.add_transition(72, c10)
c9.add_transition(73, c10)
c9.add_transition(74, c10)
c9.add_transition(75, c10)
c9.add_transition(76, c10)
c9.add_transition(77, c10)
c9.add_transition(78, c10)
c9.add_transition(79, c10)
c9.add_transition(80, c10)
c9.add_transition(81, c10)
c9.add_transition(82, c10)
c9.add_transition(83, c10)
c9.add_transition(84, c10)
c9.add_transition(85, c10)
c9.add_transition(86, c10)
c9.add_transition(87, c10)
c9.add_transition(88, c10)
c9.add_transition(89, c10)
c9.add_transition(90, c10)

c10.isFinalState = True


def tk_c10(): 
	
	with open(fileOut, 'a') as archivo:
	    # Escribe datos en el archivo
	    archivo.write("TOKEN ")
	


c10.token = tk_c10
c10.add_transition(65, c10)
c10.add_transition(66, c10)
c10.add_transition(67, c10)
c10.add_transition(68, c10)
c10.add_transition(69, c10)
c10.add_transition(70, c10)
c10.add_transition(71, c10)
c10.add_transition(72, c10)
c10.add_transition(73, c10)
c10.add_transition(74, c10)
c10.add_transition(75, c10)
c10.add_transition(76, c10)
c10.add_transition(77, c10)
c10.add_transition(78, c10)
c10.add_transition(79, c10)
c10.add_transition(80, c10)
c10.add_transition(81, c10)
c10.add_transition(82, c10)
c10.add_transition(83, c10)
c10.add_transition(84, c10)
c10.add_transition(85, c10)
c10.add_transition(86, c10)
c10.add_transition(87, c10)
c10.add_transition(88, c10)
c10.add_transition(89, c10)
c10.add_transition(90, c10)

d1.isFinalState = True


def tk_d1(): 
	
	with open(fileOut, 'a') as archivo:
	    # Escribe datos en el archivo
	    archivo.write("UPPERCASE ")
	


d1.token = tk_d1
d1.add_transition(65, d1)
d1.add_transition(66, d1)
d1.add_transition(67, d1)
d1.add_transition(68, d1)
d1.add_transition(69, d1)
d1.add_transition(70, d1)
d1.add_transition(71, d1)
d1.add_transition(72, d1)
d1.add_transition(73, d1)
d1.add_transition(74, d1)
d1.add_transition(75, d1)
d1.add_transition(76, d1)
d1.add_transition(77, d1)
d1.add_transition(78, d1)
d1.add_transition(79, d1)
d1.add_transition(80, d1)
d1.add_transition(81, d1)
d1.add_transition(82, d1)
d1.add_transition(83, d1)
d1.add_transition(84, d1)
d1.add_transition(85, d1)
d1.add_transition(86, d1)
d1.add_transition(87, d1)
d1.add_transition(88, d1)
d1.add_transition(89, d1)
d1.add_transition(90, d1)

e1.add_transition(71, e2)

e2.add_transition(78, e3)

e3.add_transition(79, e4)

e4.add_transition(82, e5)

e5.add_transition(69, e6)

e6.add_transition(32, e7)

e7.add_transition(32, e7)
e7.add_transition(65, e8)
e7.add_transition(66, e8)
e7.add_transition(67, e8)
e7.add_transition(68, e8)
e7.add_transition(69, e8)
e7.add_transition(70, e8)
e7.add_transition(71, e8)
e7.add_transition(72, e8)
e7.add_transition(73, e8)
e7.add_transition(74, e8)
e7.add_transition(75, e8)
e7.add_transition(76, e8)
e7.add_transition(77, e8)
e7.add_transition(78, e8)
e7.add_transition(79, e8)
e7.add_transition(80, e8)
e7.add_transition(81, e8)
e7.add_transition(82, e8)
e7.add_transition(83, e8)
e7.add_transition(84, e8)
e7.add_transition(85, e8)
e7.add_transition(86, e8)
e7.add_transition(87, e8)
e7.add_transition(88, e8)
e7.add_transition(89, e8)
e7.add_transition(90, e8)

e8.add_transition(32, e9)
e8.add_transition(65, e8)
e8.add_transition(66, e8)
e8.add_transition(67, e8)
e8.add_transition(68, e8)
e8.add_transition(69, e8)
e8.add_transition(70, e8)
e8.add_transition(71, e8)
e8.add_transition(72, e8)
e8.add_transition(73, e8)
e8.add_transition(74, e8)
e8.add_transition(75, e8)
e8.add_transition(76, e8)
e8.add_transition(77, e8)
e8.add_transition(78, e8)
e8.add_transition(79, e8)
e8.add_transition(80, e8)
e8.add_transition(81, e8)
e8.add_transition(82, e8)
e8.add_transition(83, e8)
e8.add_transition(84, e8)
e8.add_transition(85, e8)
e8.add_transition(86, e8)
e8.add_transition(87, e8)
e8.add_transition(88, e8)
e8.add_transition(89, e8)
e8.add_transition(90, e8)

e9.isFinalState = True


def tk_e9(): 
	
	with open(fileOut, 'a') as archivo:
	    # Escribe datos en el archivo
	    archivo.write("IGNOREFLAG ")
	


e9.token = tk_e9
e9.add_transition(32, e9)
e9.add_transition(65, e10)
e9.add_transition(66, e10)
e9.add_transition(67, e10)
e9.add_transition(68, e10)
e9.add_transition(69, e10)
e9.add_transition(70, e10)
e9.add_transition(71, e10)
e9.add_transition(72, e10)
e9.add_transition(73, e10)
e9.add_transition(74, e10)
e9.add_transition(75, e10)
e9.add_transition(76, e10)
e9.add_transition(77, e10)
e9.add_transition(78, e10)
e9.add_transition(79, e10)
e9.add_transition(80, e10)
e9.add_transition(81, e10)
e9.add_transition(82, e10)
e9.add_transition(83, e10)
e9.add_transition(84, e10)
e9.add_transition(85, e10)
e9.add_transition(86, e10)
e9.add_transition(87, e10)
e9.add_transition(88, e10)
e9.add_transition(89, e10)
e9.add_transition(90, e10)

e10.isFinalState = True


def tk_e10(): 
	
	with open(fileOut, 'a') as archivo:
	    # Escribe datos en el archivo
	    archivo.write("IGNOREFLAG ")
	


e10.token = tk_e10
e10.add_transition(65, e10)
e10.add_transition(66, e10)
e10.add_transition(67, e10)
e10.add_transition(68, e10)
e10.add_transition(69, e10)
e10.add_transition(70, e10)
e10.add_transition(71, e10)
e10.add_transition(72, e10)
e10.add_transition(73, e10)
e10.add_transition(74, e10)
e10.add_transition(75, e10)
e10.add_transition(76, e10)
e10.add_transition(77, e10)
e10.add_transition(78, e10)
e10.add_transition(79, e10)
e10.add_transition(80, e10)
e10.add_transition(81, e10)
e10.add_transition(82, e10)
e10.add_transition(83, e10)
e10.add_transition(84, e10)
e10.add_transition(85, e10)
e10.add_transition(86, e10)
e10.add_transition(87, e10)
e10.add_transition(88, e10)
e10.add_transition(89, e10)
e10.add_transition(90, e10)

f1.isFinalState = True


def tk_f1(): 
	
	with open(fileOut, 'a') as archivo:
	    # Escribe datos en el archivo
	    archivo.write("TWODOTS ")
	


f1.token = tk_f1

g1.isFinalState = True


def tk_g1(): 
	
	with open(fileOut, 'a') as archivo:
	    # Escribe datos en el archivo
	    archivo.write("SEMICOLON ")
	


g1.token = tk_g1

h1.isFinalState = True


def tk_h1(): 
	
	with open(fileOut, 'a') as archivo:
	    # Escribe datos en el archivo
	    archivo.write("OR ")
	


h1.token = tk_h1

j1.isFinalState = True


def tk_j1(): 
	
	with open(fileOut, 'a') as archivo:
	    # Escribe datos en el archivo
	    archivo.write("SPACE ")
	


j1.token = tk_j1
j1.add_transition(9, j1)

k1.isFinalState = True


def tk_k1(): 
	
	with open(fileOut, 'a') as archivo:
	    # Escribe datos en el archivo
	    archivo.write("NEWLINE ")
	


k1.token = tk_k1
k1.add_transition(10, k1)


args = parser.parse_args()
fileToRead = args.source
def exclusiveSim(initState: State, string: str):
    string += ' '
    paths: List[List[State]] = [[initState]]
    listTextTuple: List[Tuple[str, str or int]] = []
    lastPathAccepted: List[Tuple[int, List, int]] = []

    chIndex = 0
    lasChIndex = 0

    while chIndex < len(string):
        ch = string[chIndex]
        char = ord(ch)
        newPaths: List[List[State]] = []

        for path in paths:
            evalState: State = path[-1]

            for st in evalState.getStates(char):
                newPath = path.copy()
                newPath.append(st)
                newPaths.append(newPath)

        if len(newPaths) == 0:
            if len(lastPathAccepted) == 0:
                textToAccept = string[lasChIndex:chIndex + 1]
                listTextTuple.append((textToAccept, 0 if len(textToAccept) == 0 or textToAccept == ' ' else 1))
                chIndex += 1
                lasChIndex = chIndex
                paths = [[initState]]
                continue

            lastChar, lastStateAccepted, _ = lastPathAccepted[0]
            textToAccept = string[lasChIndex:lastChar + 1]
            listTextTuple.append((textToAccept, lastStateAccepted[-1].token))
            lasChIndex = lastChar + 1
            chIndex = lastChar + 1
            paths = [[initState]]
            lastPathAccepted = []
            continue

        newLastPathAccepted = []

        for path in newPaths:
            if path[-1].isFinalState:
                newLastPathAccepted.append(
                    (chIndex, path, path[-1].value))

        if len(newLastPathAccepted) > 0:
            lastPathAccepted = sorted(newLastPathAccepted, key=lambda x: x[2])

        paths = newPaths
        chIndex += 1

    return listTextTuple


CYAN = '\033[96m'
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
WHITE = '\033[97m'
RESET = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
REVERSE = '\033[7m'


if __name__ == '__main__':
    with open(fileToRead, 'r') as file:
        contents = file.read()

    print(YELLOW, 'Resultado:', RESET)
    tokens = exclusiveSim(a0, contents)
    for message, token in tokens:
        if token != 1 and token != 0:
            print(GREEN, message, RESET, '->')
            token()
        elif token == 1:
            print(RED, 'ERROR IN LINE:', message, RESET)
        