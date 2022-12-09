from classes.torreControle import TorreControle

def run():
    print("Condições da viagem: ")
    torreControle1 = TorreControle(vooPermitido=False)
    print(torreControle1,"\n")

if __name__ == "__main__":
    run()