#               Fernando Molina Arcas #
#               Procesador segmentado #
# Banco de resgitros y registros de desacoplamiento #

from memoria import *

REGISTER_BANK = {}

def fillBank():
    for i in range(16):
        REGISTER_BANK["R{}".format(i)] = i * 10
fillBank()

class Resgiter_if_id():

    __slots__ = ("instruction")

    def __init__(self):
        pass

class Register_id_exe():

    __slots__ = ("instruccion", "a", "b")

    def __init__(self):
        pass


class Register_exe_wb():

    __slots__ = ("instruccion", "c")

    def __init__(self):
        pass
