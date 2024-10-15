def dia_da_semana():
    numero = int(input("Digite um numero entre 1 e 7: "))

    dias = {
        1: "Domingo",
        2: "Segunda-feira",
        3: "Terça-feira",
        4: "Quarta-feira",
        5: "Quinta-feira",
        6: "Sexta-feira",
        7: "Sabado"
    }

    if numero in dias:
        print(f"o dia correspondente ao número {numero} é {dias[numero]}.")
    else: 
        print("Não existe dia da semana com esse número.")