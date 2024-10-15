#Recebendo valores do cateto
cat1 = float(input("Digite os catetos: "))
cat2 = float(input("Digite os catetos: "))

#Operaçao matematica para descubrir hipotenusa
hip = (cat1 * cat1) + (cat2 * cat2)
hip2 = hip**0.5

#Imprimindo Valor da Hipotenusa 
print("A hipotenusa desses catetos sera: ",hip2)