# Fernando Molina Arcas #
# Procesador Segmentado #
# Memoria de instrucciones y memoria principal#


class Instruction():

    __slots__ = ("codeOp", "ra", "rb", "rc")

    def __init__(self, codeOp = "NOP", ra = None, rb = None, rc = None):
        self.codeOp = codeOp
        self.ra = ra
        self.rb = rb
        self.rc = rc

    def __str__(self):
        if self.codeOp != "trap":
            return "{}\t{}, {}, {}".format(self.codeOp, self.ra, self.rb, self.rc)
        else:
            return "{}".format(self.codeOp)

class InstructionMemory():

    def __init__(self, fileName):
        self._list = []
        self._parseFromFile(fileName)

    def _parseFromFile(self, fileName:"String"):
        for linea in open(fileName, "r"):
            try:
                op, ra, rb, rc  = linea.strip().split()
                ra, rb, rc = ra[:-1], rb[:-1], rc
            except:
                op = linea[:-1]
                ra = rb = rc = None
            self._list.append(Instruction(op, ra, rb, rc))

    def showInstructions(self):
        for ins in self._list:
            print(ins)

    def popInstruction(self)->"instruction":
        if len(self._list) != 0:
            return self._list.pop(0)
        else:
            return Instruction()

