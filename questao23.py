def calcular_imc():
    peso = float(input("Digite o peso (em kg): "))
    altura = float(input("Digite a altura (em metros): "))

    # Cálculo do IMC
    imc = peso / (altura ** 2)

    # Definindo o grau de obesidade
    if imc < 18.5:
        grau_obesidade = "magreza"
    elif 18.5 <= imc <= 24.9:
        grau_obesidade = "Saudável"
    elif 25.0 <= imc <= 29.9:
        grau_obesidade = "Sobrepeso"
    elif 30.0 <= imc <= 34.9:
        grau_obesidade = "Obesidade grau I"
    elif 35.0 <= imc <= 39.9:
        grau_obesidade = "Obesidade Grau II"
    else:
        grau_obesidade = "Obesidade Grau III"

    # Exibindo os resultados
    print(f"Seu IMC é: {imc:.2f}")
    print(f"Grau de obesidade: {grau_obesidade}")

# chamando a função
    calcular_imc()