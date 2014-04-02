from etapas import *
from structs import *
from memoria import *


insMem = InstructionMemory("instrucciones.txt")
regBank = fillBank()

etapa_if(insMem)
etapa_id(regBank)
etapa_iss()
etapa_exe()
etapa_wb(regBank)

for i in range(16):
    print("R{0:02} -> {1:3}".format(i,regBank["r{}".format(i)]))
