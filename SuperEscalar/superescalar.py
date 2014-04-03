# Fernando Molina Arcas #
# Procesador Segmentado #

from etapas import *
from structs import *
from memoria import *

def main():
    instructionMemory = InstructionMemory("instrucciones.txt")
    nIns = len(instructionMemory)
    dataMemory = fillMemory()
    regBank = fillBank()
    trap = False

    i = 1
    while(True):

        if nIns == len(ROB) and ROB[-1].mark == "fin": break

        print("Ciclo: {}".format(i))
        i += 1


        etapa_com(regBank)

        etapa_wb(regBank)

        INSTRUCTION_WINDOW.updateWindow(ROB)

        etapa_exe()

        etapa_iss()

        etapa_id(regBank)

        etapa_if(instructionMemory)

        printRoB()

    printBank(regBank)

def printRoB():
    print("        {}".format("*" * 25))
    print("\t\t   {}".format("ROB"))
    for i in range(len(ROB)):
        print("\t   {}".format(ROB[i]))
    print("        {}".format("*" * 25))

def printBank(regBank):
    print("\t{}".format("*" * 25))
    print("\t*   {}  *".format("Banco de registros"))
    print("\t{}".format("*" * 25))
    for i in range(16):
        print("\t*\tR{0:02} -> {1:3}\t*".format(i,regBank["r{}".format(i)]))


if __name__ == "__main__":
    main()
