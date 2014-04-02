#               Fernando Molina Arcas #
#               Procesador segmentado #
# Banco de resgitros y registros de desacoplamiento         #
#       Incluimos la ventana de instrucciones aqui        #
from memoria import Instruction

INSTRUCTIONS_WB = []

def fillBank():
    dic = {}
    for i in range(16):
        dic["r{}".format(i)] = (i * 10, 1)
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
            return "{}\t{}\t{}\t{}\t{}".format(self.n, self.codeOp, self.op1, self.op2, self.dest)

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
