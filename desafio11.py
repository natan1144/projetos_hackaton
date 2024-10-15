#Rebendo o numero
num = float(input("Digite um numero maior que 0: "))

#Verificaçao para ver se o numero e maior que zero
if num <1:
    print("ERRO")
    print("DIGITE UM NUMERO MAIOR QUE ZERO")
else:
    #Operaçao matematica para elevar numero ao outro
    num2 = float(input("Digite outro numero maior que 0: "))
    conta = num2**num
    print("O resultado de", num2, "elevado a", num, "e: ",conta)

