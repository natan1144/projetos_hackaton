#Recebendo os valores de salario minimo e hora trabalhada
slrminino = float(input("Digite o salario minimo: "))
hrst = float(input("Digite a Horas Trabalhada: "))

#Declarando vairaveis e fazendo operaçoes matematicas
met = slrminino/2
hrot = hrst * met
imposto = hrot*3
porc = imposto/100
slrar = hrot - porc

#Imprimindo o salario a receber 
print("O salario a receber sera de: ", slrar)

