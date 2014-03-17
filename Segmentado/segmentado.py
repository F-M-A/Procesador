# Fernando Molina Arcas #
# Procesador Segmentado #

from etapas import *
from registros import *
from memoria import *

def main():
    instructionMemory = IntructionMemory("instrucciones.exe")

    fillBank()

    if_id   = Register_if_id()
    id_exe  = Register_id_exe()
    exe_wb  = Register_exe_wb()
    while(True):

        REGISTER_BANK = etapa_wb(exe_wb, REGISTER_BANK)

        if exe_wb.instruction.codeOp == "trap": break

        exe_wb = etapa_exe(id_exe)

        id_exe = etapa_id(if_id)

        if_id = etapa_if(instructionMemory)

if __name__=="main":
	main()
