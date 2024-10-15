def maior_menor():

#Recebendo numeros
    num1 = int(input("Digite um numero: "))
    num2 = int(input("Digite um numero: "))
    num3 = int(input("Digite um numero: "))

    #Verificando maior e menor
    maior = max(num1, num2, num3)
    menor = min(num1, num2, num3)

    #Imprimindo o numero maior e menor
    print(f"O maior numero é: {maior}")
    print(f"O menor numero é: {menor}")

#chamando a funçao
maior_menor()

