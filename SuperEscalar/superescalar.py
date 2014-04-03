# Fernando Molina Arcas #
# Procesador Segmentado #

from etapas import *
from structs import *
from memoria import *

def main():
    instructionMemory = InstructionMemory("instrucciones.txt")
    dataMemory = fillMemory()
    regBank = fillBank()
    trap = False

    i = 1
    while(True):

        print("Ciclo: {}".format(i))
        i += 1

        etapa_com(regBank)

        INSTRUCTION_WINDOW.updateWindow(ROB)

        etapa_wb(regBank)

#        if trap: break

        if i == 20: break

        etapa_exe()

        etapa_iss()

        trap = etapa_id(regBank)

        etapa_if(instructionMemory)



    for i in range(16):
        print("R{0:02} -> {1:3}".format(i,regBank["r{}".format(i)]))



if __name__ == "__main__":
    main()
