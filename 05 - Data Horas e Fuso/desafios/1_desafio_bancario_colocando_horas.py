import datetime
menu =  """
    [D] - Depositar
    [S] - Sacar
    [E] - Extrato
    [Q] - Sair
    
=> """ 

Valor_em_caixa = 0
Extrato = {}
Valor_maximo_saque = 500
limite_saque_dicionario = {} #criando dicinoario
data_atual = datetime.datetime.today().strftime("%d/%m/%Y")

      
def pega_qtde_saque_permitido():
    if data_atual not in limite_saque_dicionario:                 # Verifica se tem o registro de limite criado para o dia
    
        limite_saque_dicionario.update({data_atual:10}) # Adiciona 10 oportunidade de saque
    
    limite_de_saque_do_dia = limite_saque_dicionario[data_atual]
    return limite_de_saque_do_dia



def operacao_saque_deposito(valor, operacao):
    data_hora_atual = datetime.datetime.today().strftime("%d/%m/%Y %H:%M:%S")
    
    Extrato.update({data_hora_atual:{"valor":str(valor), "Tipo de Operação:":operacao}})
    
    print(f"A operacao de {operacao} no valor de R$ {valor:.2f} foi realizado com sucesso!")

def depositar():
    valo_sacar = float(input("Digite o valor a ser depositado:"))
    global Valor_em_caixa 
    Valor_em_caixa += valo_sacar 

    operacao_saque_deposito(valo_sacar, "deposito")

    return Valor_em_caixa


def sacar():
    global Valor_maximo_saque
    global Valor_em_caixa

    limite_de_saque_do_dia = pega_qtde_saque_permitido()

    while True:
        valor_a_ser_sacado = input("Digite o valor que deseja sacar ([Q] - Sair): ")
        try:
            valor_a_ser_sacado = float(valor_a_ser_sacado)
        except ValueError:
            break

        #Verifica se no dicionario "limite_saque_dicionario", na chave "data_atual" a sub chave "saque_permitido" tem valor zerado
        if limite_de_saque_do_dia == 0: #limite_saque == 0:
            print("Você alcançou a quantidade limite de saques no dia. Volte amanhã!")
            break
        elif valor_a_ser_sacado > Valor_maximo_saque:
            print(f"Valor maior que o limite permitido por saque, selecione um valor menor ou igual a R$ {Valor_maximo_saque:.2f}")
        elif valor_a_ser_sacado > Valor_em_caixa:
            print("O valor disponível em caixa é menor que o desejado a sacar")
            print(f"Valor em caixa: R$ {Valor_em_caixa:.2f}; valor que deseja sacar: R$ {valor_a_ser_sacado:.2f}")
        
        else:
            Valor_em_caixa -= valor_a_ser_sacado
            operacao_saque_deposito(valor_a_ser_sacado,"saque")


            limite_de_saque_do_dia -= 1 # Remove um transação permitida do dia

            limite_saque_dicionario.update({data_atual:limite_de_saque_do_dia})#Atualizando a quantidade de saques ainda permitido no dia

            break


while True:
    valor = input(menu)
    if valor == "D":
        print("\n \n==============depositar==============")   
        depositar() 
        
        
    elif valor == "S":
        print("\n \n==============Sacar==============")          
        sacar()
       
       
    elif valor == "E":
        print("\n \n==============extrato==============")

       # print("\n".join(Extrato))
        for data in Extrato:#segundo método de listar dicionario inteiro
           operacao = Extrato[data]["valor"]
           print(f"Em {data} foi realizado a operacao de {Extrato[data]['Tipo de Operação:']} no valor de R$ {Extrato[data]['valor']} ")


        print(f"o valor total disponível para saque é de: R$ {Valor_em_caixa:.2f}")
    elif valor == "Q":
        break
    else:
        print("Valor invalido, seleciona uma opção válida!")
    



