from classes.piloto import Piloto

def run():
    print("Dados do Piloto")
    piloto1 = Piloto(nome="Gabriel",idade="32",rg="1231", especializacao="Piloto de Carga")
    print(piloto1)

if __name__ == "__main__":
    run()