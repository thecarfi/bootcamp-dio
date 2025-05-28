''' 
Para ler e escrever dados em Python, utilizamos as seguintes funções: 
- input: lê UMA linha com dado(s) de Entrada do usuário;
- print: imprime um texto de Saída (Output), pulando linha.  
'''

class ContaBancaria:
    # TODO: Inicialize a conta bancária com o nome do titular, saldo 0 e  liste para armazenar as operações realizadas:
    def __init__(self,  nome_titular):
      self._nome_titular = nome_titular
      self._saldo = 0
      self.extrato_conta = ["Operações: "]
    # TODO: Implemente o método para realizar um depósito, adicione o valor ao saldo e registre a operação:

    def depositar(self, valor):
      if valor > 0:
        self._saldo +=valor
        if len(self.extrato_conta) == 1:
           self.extrato_conta.append("+" + str(valor))
        else: 
           self.extrato_conta.append(", +" + str(valor))
        
      else:

        return

    # TODO: Implemente o método para realizar um saque:
    def sacar(self,valor):
      # TODO: Verifique se há saldo suficiente para o saque

      if (self._saldo - (valor*-1)) >= 0:

        # TODO: Subtraia o valor do saldo (valor já é negativo)
        self._saldo -= (valor*-1)
        if len(self.extrato_conta) == 1:
           self.extrato_conta.append("" + str(valor))
        else:
           self.extrato_conta.append(", " + str(valor))
        # TODO: Registre a operação e retorne a  mensagem de saque negado
      else:
        if len(self.extrato_conta) == 1:
           self.extrato_conta.append(" Saque não permitido")
        else:
          self.extrato_conta.append(", Saque não permitido")
            

    # TODO: Crie o método para exibir o extrato_conta da conta e junte as operações no formato correto:
    def extrato(self):
      self.extrato_conta.append("; Saldo: " + str(self._saldo))

      for valor in self.extrato_conta:
         print(valor, end="")


nome_titular = input().strip()  

conta = ContaBancaria(nome_titular)  

entrada_transacoes = input().strip() 
transacoes = [int(valor) for valor in entrada_transacoes.split(",")]  

for valor in transacoes:
    if valor > 0:
        conta.depositar(valor)  
    else:
        conta.sacar(valor)  

conta.extrato()