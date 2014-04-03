#               Fernando Molina Arcas #
#               Procesador segmentado #
# Banco de resgitros y registros de desacoplamiento         #
#       Incluimos la ventana de instrucciones aqui        #
from memoria import Instruction

INSTRUCTIONS_WB = []

def fillBank():
    dic = {}
    for i in range(16):
        dic["r{}".format(i)] = i * 10
    return dic

class InstructionWindow():
    class InstructionLine():

        __slots__ = ("n", "codeOp", "op1", "ok1", "op2", "ok2", "dest")

        #N es el numero de la instruccion para asi poder reconocerla
        def __init__(self, n, codeOp, op1, ok1, op2, ok2, dest):
            self.n = n
            self.codeOp = codeOp
            self.op1 = op1
            self.ok1 = ok1
            self.op2 = op2
            self.ok2 = ok2
            self.dest = dest

        def __str__(self):
            return "{}\t{}\t{}\t{}\t{}\t{}\t{}".format(self.n, self.codeOp, self.op1, self.ok1,self.op2, self.ok2, self.dest)

        def __repr__(self):
            return "{}\t{}\t{}\t{}\t{}\t{}\t{}".format(self.n, self.codeOp, self.op1, self.ok1,self.op2, self.ok2, self.dest)

    MAX_INSTRUCTION = 64

    def __init__(self):
        self._list = []

    def __len__(self):
        return len(self._list)

    def pop(self, i):
        return self._list.pop(i)

    def __getitem__(self, key):
        return self._list[key]

    def addInstruction(self, n, codeOp, op1, ok1, op2, ok2, dest):
        self._list.append(self.InstructionLine(n, codeOp, op1, ok1, op2, ok2, dest))

    def __str__(self):
        return "{}".format(self._list)

    def updateWindow(self, RoB):
        for i in range(len(self._list)):
            ins = self._list[i]
            if ins.ok1 == 0 and RoB[ins.op1].ok == 1:
                self._list[i].op1 = RoB[ins.op1].res
                self._list[i].ok1 = 1

            if ins.ok2 == 0 and RoB[ins.op2].ok == 1:
                self._list[i].op2 = RoB[ins.op2].res
                self._list[i].ok2 = 1


# Suponemos un ROB infinito
class RoB():
    class RoBLine():

        # i -> n Instruccion #

        __slots__ = ("i", "dest", "codeOp", "ok", "mark", "res")

        def __init__(self, i , dest, codeOp, ok = 0, mark = "x"):
            self.i = i
            self.dest = dest
            self.codeOp = codeOp
            self.ok = ok
            self.mark = mark
            self.res = "-"

        def __str__(self):
            return "{} {} {} {} {} {}".format(self.i, self.dest, self.codeOp, self.ok, self.mark, self.res)

    def __init__(self):
        self._list = []

    def addLine(self, i, dest, codeOp):
        self._list.append(self.RoBLine(i, dest, codeOp))

    def modLine(self, n, ok, mark):
        self._list[n].ok = ok
        self._list[n].mark = mark

    def findRegAndAssign(self, i:"start", reg, regBank):
        if i == 0: return regBank[reg], 1
        for i in range(len(self._list) - 2, -1, -1):
            if self._list[i].dest == reg:
                if self._list[i].ok == 1:
                    return self._list.res, 1
                else:
                    return i, 0
            else:
                return regBank[reg], 1

    def assignRes(self, i, res):
        self._list[i].res = res
        self._list[i].ok = 1
        self._list[i].mark = "f"

    def __getitem__(self, key):
        return self._list[key]

    def __len__(self):
        return len(self._list)




