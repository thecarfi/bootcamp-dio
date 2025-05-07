menu =  """
    [D] - Depositar
    [S] - Sacar
    [E] - Extrato
    [Q] - Sair
    
=> """ 

Valor_em_caixa = 0
Extrato = []
limite_saque = 3
Valor_maximo_saque = 500


while True:
    valor = input(menu)
    if valor == "D":
        print("\n \n==============depositar==============")    
        valor_depositado = float(input("Digite o valor a ser depositado:"))
        Valor_em_caixa += valor_depositado 
        Extrato.append( f" valor de R$ {valor_depositado:.2f} depositado") 
        print(f"O valor de R$ {valor_depositado:.2f} foi depositado com sucesso!")

    elif valor == "S":
        print("\n \n==============Sacar==============")  


        while True:
            valor_a_ser_sacado = input("Digite o valor que deseja sacar ([Q] - Sair): ")
            try:
                valor_a_ser_sacado = float(valor_a_ser_sacado)
            except ValueError:
                break
            if limite_saque == 0:
                print("Você alcançou a quantidade limite de saques no dia. Volte amanhã!")
                break
            elif valor_a_ser_sacado > Valor_maximo_saque:
                print(f"Valor maior que o limite permitido por saque, selecione um valor menor ou igual a R$ {Valor_maximo_saque:.2f}")
            elif valor_a_ser_sacado > Valor_em_caixa:
                print("O valor disponível em caixa é menor que o desejado a sacar")
                print(f"Valor em caixa: R$ {Valor_em_caixa:.2f}; valor que deseja sacar: R$ {valor_a_ser_sacado:.2f}")
            
            else:
                Valor_em_caixa -= valor_a_ser_sacado
                Extrato.append(f"O valor de R$ {valor_a_ser_sacado:.2f} foi sacado")
                limite_saque -= 1
                print(f"O valor de R$ {valor_a_ser_sacado:.2f} foi sacado com sucesso!")
                break

    elif valor == "E":
        print("\n \n==============extrato==============")

        print("\n".join(Extrato))

        print(f"o valor total disponível para saque é de: R$ {Valor_em_caixa:.2f}")
    elif valor == "Q":
        break
    else:
        print("Valor invalido, seleciona uma opção válida!")
    