# Fernando Molina Arcas #
# Procesador Segmentado #
# Etapas del procesador #

from structs import InstructionWindow, INSTRUCTIONS_WB
from memoria import Instruction

MULT_CICLES = 3
LOAD_CICLES = 2
ALU_CICLES = 1


INSTRUCTION_QUEUE = []
INSTRUCTION_WINDOW = InstructionWindow()
SEGMENTATION_MULT_UNIT = [0] * MULT_CICLES
SEGMENTATION_LOAD_UNIT = [0] * LOAD_CICLES
# 4 Instrucciones pueden estar en exe a la vez #
# [ALU, ALU, MULT, MEM]
INSTRUCTIONS_IN_EXE = [0] * 4


CODE_OP_MAP = {"add": 1, "sub" : 2, "mult" : 3,\
               "div": 4, "lw"  : 5, "sw"   : 6,\
               "trap":-1, "nop": 0}


def etapa_if(insMem:"InstructionMemory") -> "Register_if_id":
    INSTRUCTION_QUEUE.append(insMem.popInstruction())
    INSTRUCTION_QUEUE.append(insMem.popInstruction())

def etapa_id(regBank, rob = None) -> "Register_id_exe":
    for i in range(2):
        n      = INSTRUCTION_QUEUE[i].n
        codeOp = INSTRUCTION_QUEUE[i].codeOp
        dest     = INSTRUCTION_QUEUE[i].ra
        rb     = INSTRUCTION_QUEUE[i].rb
        rc     = INSTRUCTION_QUEUE[i].rc

        ok1 = regBank[rb][1]
        op1 = regBank[rb][0] if ok1 == 1 else rb
        ok2 = regBank[rc][1]
        op2 = regBank[rc][0] if ok2 == 1 else rc
        codeOp = CODE_OP_MAP[codeOp]

        INSTRUCTION_WINDOW.addInstruction(n, codeOp, op1, ok1, op2, ok2, dest)
        regBank[dest] = (regBank[dest], 0)

def etapa_iss():
    i = 0
    iss = False
    removable = []
    for i in range(len(INSTRUCTION_WINDOW)):
        ins = INSTRUCTION_WINDOW[i]
        if ins.ok1 and ins.ok2:
            iss = True
            if 1<=ins.codeOp<=2:
                if INSTRUCTIONS_IN_EXE[0] == 0:
                    INSTRUCTIONS_IN_EXE[0] == ins
                elif INSTRUCTIONS_IN_EXE[1] == 0:
                    INSTRUCTIONS_IN_EXE[1] = ins

            elif 3<=ins.codeOp<=4 and INSTRUCTIONS_IN_EXE[2] == 0:
                INSTRUCTIONS_IN_EXE[2] = ins

            else: pass
        if iss:
            removable.append(i)
            iss = False

    removable.reverse()
    for i in removable:
        INSTRUCTION_WINDOW.pop(i)


def etapa_exe() -> "Register_exe_wb":
    for i in range(len(INSTRUCTIONS_IN_EXE)):
        ins = INSTRUCTIONS_IN_EXE[i]
        res = False
        if 0<=i<=1: #ALU
            if ins == 1:
                out = ins.op1 + ins.op2
                res = True
            elif ins == 2:
                out = ins.op1 - ins.op2
                res = True

        elif i == 2: #MDU
            pass

        if res:
            INSTRUCTIONS_WB.append((ins.dest, out))
            INSTRUCTIONS_IN_EXE[i] = 0

def etapa_wb(registerBank) -> "Map, instruction":
    for i in range(2):
        try: ins = INSTRUCTIONS_WB.pop(0)
        except: ins = None
        if ins != None:
            registerBank[ins[0]] = (ins[1], 1)


def etapa_com():
    pass
