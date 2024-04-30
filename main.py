from subprocess import run
from Simulator import *
from reader import reader
from Tree_ import make_direct_tree, make_tree
from Draw_diagrams import draw_tree
from typing import Dict
from preAFD import *
import yalexReader
from Colors import BOLD, REVERSE, GREEN, YELLOW, RESET

yr = yalexReader.YalexReader('lexer1.yal')
yr.analizeFile()
yr.createScanners()