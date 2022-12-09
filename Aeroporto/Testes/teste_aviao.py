from classes.aviao import Aviao

def run():
    print("Dados do aviao: ")
    boeing = Aviao(modelo="Boeing 747", cargaMax="78")
    print(boeing,"\n")

if __name__ == "__main__":
    run()