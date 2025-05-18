#Quando usado _ no inicio de uma variavel, é convencionado que esta é privada (acessavel apenas por funções da classe)
class conta:
    def __init__(self,numero_agencia, saldo=0,):
        self._saldo = saldo
        self.numero_agencia = numero_agencia
    def depositar(self,valor):
        self._saldo += valor
    
    def sacar(self,valor):
        self._saldo -= valor

    def consultar_saldo(self):
        return self._saldo



conta = conta("0001",100)



print(conta._saldo)
print(conta.numero_agencia)
print(conta.consultar_saldo())