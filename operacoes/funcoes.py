#definindo função
def exibir_mensagem():
    print("teste")


nome = str(input("digite o seu nome: "))
def exbir_mensagem_com_nome(nome):
    print(f"olá, {nome}")

exibir_mensagem()    
exbir_mensagem_com_nome(nome)



def retorno_antecessor_e_sucessor(numero):
    antecessor = numero-1
    sucessor = numero+1

    return antecessor, sucessor

print(retorno_antecessor_e_sucessor(2))