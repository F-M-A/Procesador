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

        exe_wb = etapa_exe(id_exe, dataMemory)

        if exe_wb.instruction.codeOp == "trap": break

        id_exe, retorno = etapa_id(if_id, id_exe, registerBank)
        if retorno: continue

        if_id = etapa_if(instructionMemory)
    for i in range(16):
        print("R{0:02} -> {1:3}".format(i,registerBank["r{}".format(i)]))


if __name__ == "__main__":
    main()
