import sys, os

from classes.torreControle import TorreControle
from classes.aeroporto import Aeroporto

class Voo(TorreControle, Aeroporto):
    def __init__(self, vooPermitido="", nome=""):
        super().__init__(vooPermitido, nome)

    # Disable Print
    def blockPrint():
        sys.stdout = open(os.devnull, 'w')

    # Restore Print
    def enablePrint():
        sys.stdout = sys.__stdout__

    def interromper(self):
        if self.vooPermitido == False:
            return self.blockPrint()
        else:
            return self.enablePrint()

    def __str__(self):
        return f"O voo se iniciará do aeroporto"