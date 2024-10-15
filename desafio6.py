#Recebendo o Valor do Salario
sb = float(input("Digite seu salario base: "))

#Operaçao de Porcetagem
sf = sb*10
sf2 = sf/100

#Operaçao pra descubrir o salario final
resultado = sb - sf2
grf = resultado + 50

#Imprimindo Salario Final
print("O salario final vai ficar: ", grf)