#não é obrigado a utilizar o termo args e kwargs para passar na função

def exibir_poema(data_extenso, *args, **kwargs):
    
    # texto recebe o valor args e para cada unidade desse vetor, ele concatena quebrando uma linha
    texto = "\n".join(args)

    #recebe o kwargs e alinha para "chave = valor"
    meta_dados = "\n".join([f"{chave.title()}== {valor}" for chave, valor in kwargs.items()])

    #organiza todo o texto que será printado
    mesangem = f"{data_extenso} \n \n {texto} \n \n {meta_dados}"

    print(mesangem)

exibir_poema("teste data", "teste 1 args", "teste 2 args", "teste 3 args", teste_1="kwargs1", teste_2="kwargs2")