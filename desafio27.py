#Funçao para calcular a data de desvoluçao com base no tipo de usuario
def calcular_data_devoluçao(data_emprestimo, tipo_usuario):
    #Divide a data de emprestimo em dia, mes e ano
    dia, mes, ano = map(int, data_emprestimo.split("/"))

    #Define o numero de dias para devolver com base no tipo de usuario
    if tipo_usuario.lower() == "professora":
        dias_para_devoluçao = 20
    elif tipo_usuario.lower() == "aluno":
        dias_para_devoluçao = 15
    else:
        return "tipo de usuario invalido"
    
    #Calcula a data de devoluçao
    dia += dias_para_devoluçao

    #Ajusta o mes e o dia se passar de 30 dias 
    if dia > 30:
        dia-=30
        mes += 1
    
    #AJusta o ano se passar de dezembro
        if mes > 12:
            dia -= 30
            mes += 1
    #Formata a data de devoluçao para a impressao
            return f"{dia:02d}/{mes:02d}/{ano}"


#Solicita informaçoes do usuario
nome_livro = input("Nome do Livro: ")
tipousu = input("Tipo de Usuario (Professor/Aluno): ")
dtemprestimo = input("Data do emprestimo (dd/mm/aaaa): ")

#Calcula a data de revoluçao
data_devoluçao = calcular_data_devoluçao

#Exibi o recibo
print("\nRecibo:")
print(f"Nome do Livro: {nome_livro}")
print(f"Tipo de usuario: {tipousu}")
print(f"Data do emprestimo: {dtemprestimo}")
print(f"Data de Devoluçao: {data_devoluçao}")


