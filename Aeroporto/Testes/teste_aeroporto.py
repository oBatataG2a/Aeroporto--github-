from classes.aeroporto import Aeroporto

def run():
    print("Dados do aeroporto: ")
    blumenau = Aeroporto(nome="Aeroporto Regional de Blumenau", estado="Santa Catarina", cidade="Blumenau")
    print(blumenau,"\n")

if __name__ == '__main__':
    run()