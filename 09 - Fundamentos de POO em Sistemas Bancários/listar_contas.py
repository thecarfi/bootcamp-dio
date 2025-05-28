''' 
Para ler e escrever dados em Python, utilizamos as seguintes funções: 
- input: lê UMA linha com dado(s) de Entrada do usuário;
- print: imprime um texto de Saída (Output), pulando linha.  
'''
contas = []

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

#TODO: Implemente a classe SistemaBancario:
class SistemaBancario:



    # TODO: Inicialize a lista de contas:

    

    # TODO: Crie uma nova conta e adicione à lista de contas:
    @classmethod
    def criar_conta(self, titular, saldo):
      
      if len(contas) == 0:
        contas.append(titular + ": R$ " + str(saldo))
      else:
        contas.append(", " + titular + ": R$ " + str(saldo) )

    # TODO: Liste todas as contas no formato "Titular: R$ Saldo":
    def listar_contas(self):

        for conta in contas:
            print(conta, end="")

#TODO: Crie uma instância de SistemaBancario:


sistema = SistemaBancario()

while True:
    entrada = input().strip()
    if entrada.upper() == "FIM":  
        break

    titular, saldo = entrada.split(", ")

    sistema.criar_conta(titular, int(saldo))

sistema.listar_contas()