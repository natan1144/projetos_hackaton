#Recebendo o valor do peso 
peso = float(input("Digite o seu peso: "))

#Operaçao matematica de porcentagem 
porc = peso*15
div = porc/100

#Imprimindo o peso da pessoa mais gorda
print(f"O novo peso, caso a pessoa engorde 15% sobre o seu peso original: {peso + div}")

#Operaçao matematica de porcentagem
porc2 = peso*20
div2 = porc/100

#Imprimindo o peso da pessoa mais magra
print(f"O novo peso, caso a pessoa emagreça 20% sobre o seu peso original: {peso - div2}")


