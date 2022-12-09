from classes.voo import Voo

def run():
    print("Condições da viagem: ")
    voo1 = Voo(name="Por que existimos?", valor="98,25", assentos=10)
    print(voo1,"\n")

if __name__ == "__main__":
    run()