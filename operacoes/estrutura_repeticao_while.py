opcao = -1

while opcao != 0:
    opcao = int(input("[1] Sacar \n [2] Extrato \n [0]"))

    if opcao == 1:
        print("sacando...")
    elif opcao == 2:
        print("Exibindo extrato...")
    elif opcao == 0:
        print("saindo...")
    else: 
        print("operacao invalida")