# Fernando Molina Arcas #
# Procesador Segmentado #
# Memoria de instrucciones y memoria principal#


"""
El formato de las instrucciones:
    add ra,  rb, rc
    sw  ra, inm, rc

    En las instrucciones de carga y descarga el inmediato estará ubicado
    en el medio hay que tener cuidado

    Para el procesador superescalar se añade una nueva variable que indica
    el numero de ciclos que estara la instruccion en la etapa exe
"""
class Instruction():

    __slots__ = ("n", "codeOp", "ra", "rb", "rc")

    def __init__(self, n = 0, codeOp = "nop", ra = None, rb = None, rc = None):
        self.n = n
        self.codeOp = codeOp.lower()
        self.ra = ra
        self.rb = rb
        self.rc = rc

    def __str__(self):
        if self.codeOp != "trap":
            return "{}\t{}, {}, {}".format(self.codeOp, self.ra, self.rb, self.rc)
        else:
            return "{}".format(self.codeOp)

    def __repr__(self):
        if self.codeOp != "trap":
            return "({}, {}, {}, {}, {})".format(self.n, self.codeOp, self.ra, self.rb, self.rc)
        else:
            return "{}".format(self.codeOp)


class InstructionMemory():

    def __init__(self, fileName):
        self._list = []
        self._parseFromFile(fileName)

    def _parseFromFile(self, fileName:"String"):
        i = 0;
        for linea in open(fileName, "r"):
            try:
                op, ra, rb, rc  = linea.strip().split()
                ra, rb, rc = ra[:-1], rb[:-1], rc
            except:
                op = linea[:-1]
            self._list.append(Instruction(i, op, ra, rb, rc))
            i += 1

    def showInstructions(self):
        for ins in self._list:
            print(ins)

    def popInstruction(self)->"instruction":
        if len(self._list) != 0:
            return self._list.pop(0)
        else:
            return Instruction()

def fillMemory():
    out = []
    for i in range(32):
        out.append(i * 100)
    return out
