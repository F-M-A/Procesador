# Fernando Molina Arcas #
# Procesador Segmentado #

from etapas import *
from registros import *
from memoria import *

def main():
    instructionMemory = InstructionMemory("instrucciones.txt")
    dataMemory = None

    registerBank = fillBank()

    if_id   = Register_if_id()
    id_exe  = Register_id_exe()
    exe_wb  = Register_exe_wb()

    i = 0
    while(True):
        print("Ciclo: {}".format(i))
        i += 1
        registerBank = etapa_wb(exe_wb, registerBank)

        if exe_wb.instruction.codeOp == "trap": break

        exe_wb = etapa_exe(id_exe)

        id_exe, retorno = etapa_id(if_id, id_exe, registerBank)
        if retorno: continue

        if_id = etapa_if(instructionMemory)
    for i in range(16):
        print("R{0:02} -> {1:3}".format(i,registerBank["r{}".format(i)]))
main()
