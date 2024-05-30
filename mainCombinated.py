from Simulator import *
from reader import reader
from Tree_ import make_direct_tree, make_tree
from Draw_diagrams import draw_tree
from typing import Dict
from preAFD import *
import yalexReader
import subprocess
from yaparReader import YaparReader
from Colors import BOLD, REVERSE, GREEN, YELLOW, RESET

if __name__ == "__main__":
    yr = yalexReader.YalexReader('Slr-1.yal')
    yr.analizeFile()
    yr.createScanners()

    scannerPath = './scanner/out_tokens.py'
    tokensPath = './scanner/Salida.txt'
    
    readTokens = ['python', scannerPath, './scanner/asd1.txt', '-o', tokensPath]
    subprocess.run(readTokens) 
    
    with open(tokensPath, 'r') as file:
        content = file.read()
    readerYapar = YaparReader("./slr-1.yalp")
    readerYapar.analizeFile()
    readerYapar.drawLR0()
    readerYapar.drawLR0(True)
    readerYapar.constructSLR()
    readerYapar.SLR.simulation(content)