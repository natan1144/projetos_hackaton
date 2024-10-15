#Lista de vogais
vogais = ["a","e","i","o","u"]

#Recebendo a letra
letra = input("Digite uma letra: ")

#Verificando se e vogal ou consoante
if letra in vogais:
    print("A letra e Vogal")
else:
    print("A letra e consoante")