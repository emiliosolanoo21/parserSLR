from yaparReader import YaparReader

if __name__ == '__main__':
    tokensPath = './scanner/Salida.txt'
    with open(tokensPath, 'r') as file:
        content = file.read()
    readerYapar = YaparReader("./slr-3.yalp")
    readerYapar.analizeFile()
    readerYapar.drawLR0()
    readerYapar.drawLR0(True)
    readerYapar.constructSLR()
    readerYapar.SLR.simulation(content)