#               Fernando Molina Arcas #
#               Procesador segmentado #
# Banco de resgitros y registros de desacoplamiento #

from memoria import Instruction

REGISTER_BANK = {}

def fillBank():
    for i in range(16):
        REGISTER_BANK["R{}".format(i)] = i * 10

class Register_if_id():

    __slots__ = ("instruction")

    def __init__(self, instruction = Instruction()):
        self.instruction = instruction

class Register_id_exe():

    __slots__ = ("instruccion", "a", "b")

    def __init__(self, instruction = Instruction(), a = None, b = None):
        self.instruction = instruction
        self.a = a; self.b = b

class Register_exe_wb():

    __slots__ = ("instruccion", "c")

    def __init__(self, instruction = Instruction(), c = None):
        self.instruction = instruction
        self.c = c
