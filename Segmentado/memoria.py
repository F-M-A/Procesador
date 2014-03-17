# Fernando Molina Arcas #
# Procesador Segmentado #
# Memoria de instrucciones y memoria principal#


class Instruction():

    __slots__ = ("codeOp", "ra", "rb", "rc")

    def __init__(self, codeOp, ra, rb, rc):
        self.codeOp = codeOp
        self.ra = ra
        self.rb = rb
        self.rc = rc

    def __str__(self):
        return "{}\t{}, {}, {}".format(self.codeOp, self.ra, self.rb, self.rc)

class InstructionMemory():

    def __init__(self, fileName):
        self._list = []
        self._parseFromFile(fileName)

    def _parseFromFile(self, fileName:"String"):
        for linea in open(fileName, "r"):
            op, ra, rb, rc  = linea.strip().split()
            ra, rb, rc = ra[:-1], rb[:-1], rc
            self._list.append(Instruction(op, ra, rb, rc))

    def showInstructions(self):
        print(self._list[0])

    def popInstruction(self)->"instruction":
        return self.__lista.pop(0)

INSTRUCTION_MEMORY = InstructionMemory("instrucciones.txt")
INSTRUCTION_MEMORY.showInstructions()
