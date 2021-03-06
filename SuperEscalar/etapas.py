# Fernando Molina Arcas #
# Procesador Segmentado #
# Etapas del procesador #

from structs import InstructionWindow, INSTRUCTIONS_WB, RoB
from memoria import Instruction
import sys

MULT_CYCLES = 3
LOAD_CYCLES = 2
ALU_CYCLES = 1


INSTRUCTION_QUEUE = []
INSTRUCTION_WINDOW = InstructionWindow()
SEGMENTATION_MULT_UNIT = [0] * MULT_CYCLES
SEGMENTATION_LOAD_UNIT = [0] * LOAD_CYCLES
# 4 Instrucciones pueden estar en exe a la vez #
# [ALU, ALU, MULT, MEM]
INSTRUCTIONS_IN_EXE = [0] * 4

ROB = RoB()

CODE_OP_MAP = {"add": 1, "sub" : 2, "mul" : 3,\
               "div": 4, "lw"  : 5, "sw"   : 6,\
               "trap":-1, "nop": 0}


def etapa_if(insMem:"InstructionMemory") -> "Register_if_id":
    for i in range(2):
        ins = insMem.popInstruction()
        if ins != None:
            INSTRUCTION_QUEUE.append(ins)

def etapa_id(regBank) -> "Register_id_exe":
    if len(INSTRUCTION_QUEUE) > 0:
        for i in range(2):

            try: ins = INSTRUCTION_QUEUE.pop(0)
            except: return None

            n = ins.n; codeOp = ins.codeOp

            dest   = ins.ra
            rb = ins.rb; rc = ins.rc

            ROB.addLine(n, dest, codeOp)

            if codeOp != "sw":
                op1, ok1 = ROB.findRegAndAssign(n, rb, regBank)
            else: op1, ok1 = ROB.findRegAndAssign(n, dest, regBank)

            op2, ok2 = ROB.findRegAndAssign(n, rc, regBank)

            codeOp = CODE_OP_MAP[codeOp]

            INSTRUCTION_WINDOW.addInstruction(n, codeOp, op1, ok1, op2, ok2, n)

def etapa_iss():
    i = 0
    iss = False
    removable = []
    for i in range(len(INSTRUCTION_WINDOW)):
        ins = INSTRUCTION_WINDOW[i]
        if ins.ok1 and ins.ok2:
            if 1<=ins.codeOp<=2:

                if INSTRUCTIONS_IN_EXE[0] == 0:
                    INSTRUCTIONS_IN_EXE[0] = ins
                    iss = True
                elif INSTRUCTIONS_IN_EXE[1] == 0:
                    INSTRUCTIONS_IN_EXE[1] = ins
                    iss = True

            elif 3 <= ins.codeOp <= 4 and INSTRUCTIONS_IN_EXE[2] == 0:
                INSTRUCTIONS_IN_EXE[2] = ins
                iss = True

            elif 5 <= ins.codeOp <= 6 and INSTRUCTIONS_IN_EXE[3] == 0:
                INSTRUCTIONS_IN_EXE[3] = ins
                iss = True
        if iss:
            removable.append(i)
            iss = False

    removable.reverse()
    for i in removable:
        INSTRUCTION_WINDOW.pop(i)

def updateMultSegmentation():
    ins = SEGMENTATION_MULT_UNIT.pop()
    SEGMENTATION_MULT_UNIT.insert(0, 0)

    if ins != 0: INSTRUCTIONS_WB.append(ins)

def updateMemSegmentation():
    ins = SEGMENTATION_LOAD_UNIT.pop()
    SEGMENTATION_LOAD_UNIT.insert(0, 0)

    if ins != 0: INSTRUCTIONS_WB.append(ins)

def etapa_exe(dataMemory) -> "Register_exe_wb":
    for i in range(len(INSTRUCTIONS_IN_EXE)):
        ins = INSTRUCTIONS_IN_EXE[i]
        res = False
        if 0<=i<=1 and ins != 0: #ALU
            if ins.codeOp == 1: #ADD
                out = (ins.dest, ins.op1 + ins.op2)
                res = True
            elif ins.codeOp == 2: #SUB
                out = (ins.dest,ins.op1 - ins.op2)
                res = True

        elif i == 2 and ins != 0: #MDU
            if ins.codeOp == 3: #mul
                SEGMENTATION_MULT_UNIT[0] = (ins.dest, ins.op1 * ins.op2)
                INSTRUCTIONS_IN_EXE[i] = 0

        elif i == 3 and ins != 0: #MEM
            if ins.codeOp == 5: #lw
                SEGMENTATION_LOAD_UNIT[0] = (ins.dest, dataMemory[(ins.op1 + ins.op2) // 100])
                INSTRUCTIONS_IN_EXE[i] = 0
            elif ins.codeOp == 6: #sw
                SEGMENTATION_LOAD_UNIT[0] = (ins.dest, 0 + ins.op2)
                INSTRUCTIONS_IN_EXE[i] = 0

        if res:
            INSTRUCTIONS_WB.append(out)
            INSTRUCTIONS_IN_EXE[i] = 0
    updateMultSegmentation()
    updateMemSegmentation()

def etapa_wb(registerBank) -> "Map, instruction":
    for i in range(2):
        try: ins = INSTRUCTIONS_WB.pop(0)
        except: ins = None
        if ins != None:
            ROB.assignRes(ins[0], ins[1])



def etapa_com(regBank, dataMemory):
    for i in range(len(ROB)):
        ins = ROB[i]
        if ins.mark == "f" or ins.mark == "fin":
            if ins.mark == "f" and ins.codeOp != "sw":
                regBank[ins.dest] = ins.res
            elif ins.mark == "f" and ins.codeOp == "sw":
                dataMemory[ins.res // 100] = regBank[ins.dest]
            ROB[i].mark = "fin"
        else: break
