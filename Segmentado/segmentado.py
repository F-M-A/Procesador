# Fernando Molina Arcas #
# Procesador Segmentado #

from etapas import *
from registros import *
from memoria import *

def main():
    instructionMemory = InstructionMemory("instrucciones.txt")
    dataMemory = fillMemory()
    registerBank = fillBank()

    if_id   = Register_if_id()
    id_exe  = Register_id_exe()
    exe_wb  = Register_exe_wb()

    i = 1
    while(True):
        print("Ciclo: {}".format(i))
        i += 1
        registerBank, inst = etapa_wb(exe_wb, registerBank)
        print("Finalizada: {}".format(inst))

        exe_wb = etapa_exe(id_exe, dataMemory)
        print("EXE_WB: {}".format(exe_wb))

        if exe_wb.instruction.codeOp == "trap": break

        id_exe, retorno = etapa_id(if_id, id_exe, registerBank)
        print("ID_EXE: {}".format(id_exe))
        if retorno: continue

        if_id = etapa_if(instructionMemory)
        print("IF_ID: {}".format(if_id))

    printMemAndBank(registerBank, dataMemory)


def printMemAndBank(regBank, dataMemory):
    print("\t{}\t{}".format("*" * 25, "*" * 25))
    print("\t*   {}    *".format("Memoria de datos"), end = "")
    print("\t*   {}  *".format("Banco de registros"))
    print("\t{}\t{}".format("*" * 25, "*" * 25))
    for i in range(32):
        print("\t*\t{0:4} -> {1:04}\t*".format(i * 100, dataMemory[i]), end = "")
        if i < 16:
            print("\t*\tR{0:02} -> {1:3}\t*".format(i,regBank["r{}".format(i)]))
        else: print()

if __name__ == "__main__":
    main()
