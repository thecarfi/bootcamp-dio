from abc import ABC, abstractmethod
from datetime import datetime

class cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.conta = []
    
    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)
    
    def adicionar_conta(self, conta):
        self.contas.append(conta)

class pessoaFisica(cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

class conta:
    def __init__(self,numero,cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = historico()

    @classmethod #permite instanciar uma classe a partir desse objeto
    def nova_conta(cls, cliente, numero):
        return cls(numero,cliente)

    @property  #permite instanciar sem instanciar a classe pai
    def saldo(self):
        return self._saldo

    @property  #permite instanciar sem instanciar a classe pai
    def numero(self):
        return self._numero

    @property  #permite instanciar sem instanciar a classe pai
    def agencia(self):
        return self._agencia
    
    @property  #permite instanciar sem instanciar a classe pai
    def cliente(self):
        return self._cliente
    
    @property  #permite instanciar sem instanciar a classe pai
    def historico(self):
        return self._historico

    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("operação falhou, saldo insuficiente")
        
        elif valor > 0:
            self._saldo -= valor
            print("saque realizado")
            return True
        else:
            print("operação falhou, valor informado é invalido")
        return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("deposito realizado")
        else:
            print("operação falou, valor invalido")
            return False
        return True

class contaCorrente(conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3): #inicializando os atributos
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques
    
    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == "saque"]
        )

        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self.limite_saques

        if excedeu_limite:
            print("operação falou o valor do saque excede o limite")
        
        elif excedeu_saques:
            print("operação falhou numero maximo de saque excedido")
        
        else:
            return super().sacar(valor)
        
        return False
    
    def __str__(self):
        return f"""\
                Agencia: {self.agencia}
                C/C: {self.numero}
                Titular: {self.cliente.nome}
        """


class historico:
    def __init__(self): #inicalizando o atributo transação (definindo o estado inicial)
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes
    

    def adicionar_transacao(self, transacao):
        self._transacoes.append({
            "tipo": transacao.__class__.__name__
            , "valor": transacao.valor
            , "data": datetime.now().strftime ("%d-%m-%Y %H:%M:%s"),
        })


class transacao:

    @property
    @abstractmethod
    def valor(self):
        pass

    @classmethod
    @abstractmethod
    def registrar(self, conta):
        pass

class saque(transacao):
    def __init__(self,valor): #inicializando o atributo
        self._valor = valor

        @property
        def valor(self):
            return self._valor
        
        def registrar(self, conta):
            sucesso_transacao = conta.scar(self.valor)

            if sucesso_transacao:
                conta.historico.adicionar_transacao(self)

class deposito(transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)
        
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)