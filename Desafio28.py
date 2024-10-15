#Funçao para determinar o mes de vencimento
def mes_venc_ipva(placa):
    #Pega o ultimo difito da placa
    ultimo_digito = int(placa[-1])


        #Dicionario para mpear o ultimo digito ao mes de vencimento
    meses = {
        0: "Janeiro",
        1: "Fevereiro",
        2: "Março",
        3: "Abril",
        4: "Maio",
        5: "Junho",
        6: "Julho",
        7: "Agosto",
        8: "Setembro",
        9: "Outubro"
    }

    #Retorna o mes correspondende
    return meses.get(ultimo_digito, "Mes invalido")

#Solicita a placa do usuario
placa = input("Digite os 4 numeros da placa do veiculo: ")

#Exibe o mes de vencimento do IPVA
print("O mes de vencimento do IPVA é: ", mes_venc_ipva(placa))