#               Fernando Molina Arcas #
#               Procesador segmentado #
# Banco de resgitros y registros de desacoplamiento #

from memoria import Instruction

def fillBank():
    dic = {}
    for i in range(16):
        dic["r{}".format(i)] = i * 10
    return dic

class Register_if_id():

    __slots__ = ("instruction")

    def __init__(self, instruction = Instruction()):
        self.instruction = instruction

    def __str__(self):
        return "{}".format(self.instruction)

class Register_id_exe():

    __slots__ = ("instruction", "a", "b", "store")

    def __init__(self, instruction = Instruction(), a = None, b = None, store = None):
        self.instruction = instruction
        self.a = a; self.b = b
        self.store = store

    def __str__(self):
        return "{}".format(self.instruction)

class Register_exe_wb():

    __slots__ = ("instruction", "c")

    def __init__(self, instruction = Instruction(), c = None):
        self.instruction = instruction
        self.c = c

    def __str__(self):
        return "{}".format(self.instruction)
