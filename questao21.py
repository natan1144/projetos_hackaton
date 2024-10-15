def divisivel():
    a = float(input("Digite o número A: "))
    b = float(input("Digite o número B: "))

    if b != 0:
        if a % b == 0:
            print(f"{a} é divisível por {b}")
        else:
            print(f"{a} não é divisível por {b}")
    else:
        print("Divisão por zero não é permitida")

# Chamando a função
divisivel()