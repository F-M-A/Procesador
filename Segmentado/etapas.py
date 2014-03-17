# Fernando Molina Arcas #
# Procesador Segmentado #
# Etapas del procesador #

from registros import Register_if_id, Register_id_exe, Register_exe_wb
from memoria import Instruction

def etapa_if(insMem:"InstructionMemory") -> "Register_if_id":
    return Register_if_id(insMem.popInstruction())

def etapa_id(if_id, id_exe, regBank) -> "Register_id_exe":
    rb = if_id.instruction.rb; rc = if_id.instruction.rc
    codeOp = if_id.instruction.codeOp

    a = regBank[rb] if codeOp != "NOP" and codeOp != "trap" else None
    b = regBank[rc] if codeOp != "NOP" and codeOp != "trap" else None

    dest        = None if id_exe.instruction.codeOp == "sw" else rc
    leftEle     = rb
    rightEle    = None if codeOp == "lw" else rc

    if (codeOp != "NOP" and codeOp != "trap" and\
            id_exe.instruction.codeOp != "NOP" and id_exe.instruction.codeOp != "trap") and \
            (leftEle == dest or rightEle == dest):
        print("NOP introducida")
        return Register_id_exe(Instruction(), None, None), True

    return Register_id_exe(if_id.instruction, a, b), False

def etapa_exe(id_exe) -> "Register_exe_wb":
    codeOp = id_exe.instruction.codeOp
    c = None
    if codeOp == "add":
        c = id_exe.a + id_exe.b
    elif codeOp == "sub":
        c = id_exe.a - id_exe.b
    elif codeOp == "mul":
        c = id_exe.a * id_exe.b
    elif codeOp == "div":
        c = id_exe.a / id_exe.b
    elif codeOp == "lw":
        c = None
    elif codeOp == "sw":
        c = None

    return Register_exe_wb(id_exe.instruction, c)

def etapa_wb(exe_wb, registerBank) -> "Map":
    if exe_wb.instruction.codeOp != "NOP":
        registerBank[exe_wb.instruction.ra] = exe_wb.c
    return registerBank

