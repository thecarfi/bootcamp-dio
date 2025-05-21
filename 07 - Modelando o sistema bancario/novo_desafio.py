from abc import ABC, abstractmethod
from datetime import datetime
import datetime

class cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []
 
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
        self._limite = limite
        self._limite_saques = limite_saques
    
    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == saque.__name__]
        )

        excedeu_limite = valor > self._limite
        excedeu_saques = numero_saques >= self._limite_saques

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

class transacao(ABC):

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
            sucesso_transacao = conta.sacar(self.valor)

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

############################################################

menu =  """
    [D] - Depositar
    [S] - Sacar
    [E] - Extrato
    [NC] - Nova conta
    [NU] - Novo usuario
    [LC] - Lista contas
    [Q] - Sair
    
=> """ 
 
limite_saque_dicionario = {} #criando dicinoario
usuarios = [] #lista de usuarios do banco
contas = [] #lista de contas 
data_atual = datetime.datetime.today().strftime("%d/%m/%Y")
agencia ="0001"

      
def pega_qtde_saque_permitido():
    if data_atual not in limite_saque_dicionario:                 # Verifica se tem o registro de limite criado para o dia
    
        limite_saque_dicionario.update({data_atual:10}) # Adiciona 10 oportunidade de saque
    
    limite_de_saque_do_dia = limite_saque_dicionario[data_atual]
    return limite_de_saque_do_dia

def operacao_saque_deposito(valor, operacao):
    data_hora_atual = datetime.datetime.today().strftime("%d/%m/%Y %H:%M:%S")
    
    Extrato.update({data_hora_atual:{"valor":str(valor), "Tipo de Operação:":operacao}})
    
    print(f"A operacao de {operacao} no valor de R$ {valor:.2f} foi realizado com sucesso!")

def filtrar_cliente(CPF, clientes):
    clientes_filtrado = [cliente for cliente in clientes if cliente.cpf == CPF]
    return clientes_filtrado[0] if clientes_filtrado else None

def recuperar_conta_cliente(clientes):
    if not clientes.contas:
        print("cliente não possui conta")
        return
    # FIXME: não permite cliente escolher a conta
    return clientes.contas[0]

def depositar(clientes):
    cpf = input("informe o cpf do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("cliente não encontrado")
        return

    valo_sacar = float(input("Digite o valor a ser depositado:"))
    
    transacao = deposito(valo_sacar)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    cliente.realizar_transacao(conta,transacao)

def sacar(clientes):
    cpf = input("qual seu cpf? ")
    cliente = filtrar_cliente(cpf,clientes)

    if not cliente:
        print("cliente não encontrado")
        return
     
    valor = float(input("qual o valor deseja sacar? "))
    transacao = saque(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    cliente.realizar_transacao(conta,transacao)

def criar_conta(numero_conta, clientes, contas):
    print("criar conta")

    print(numero_conta)
    print(str(clientes))
    print(contas)

    CPF = input("digite o cpf")
    CPF_ja_existe = filtrar_cliente(CPF, clientes)
    
    print("CPF_ja_existe = ")
    print(CPF_ja_existe)

    if not CPF_ja_existe:
        print("cliente não encontrado")
        return
    
    conta = contaCorrente.nova_conta(cliente=CPF_ja_existe, numero=numero_conta)
    print("parte 1")
    contas.append(conta)
    print(conta)
    print("parte 2")
    cliente.contas.append(conta)
    print("parte 3")


def criar_cliente(clientes):
    CPF = input("Qual cpf: ")

    CPF_ja_existe = filtrar_cliente(CPF, clientes)

    if CPF_ja_existe:
        print("CPF ja existe cadastrado")
        return 
    print("Você não é cadastrado")
    nome = input("Qual seu nome: ")
    data_nascimento = input("Qual sua data de nascimento: ")
    endereco  = input("Qualo seu endereço: ")

    cliente = pessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=CPF, endereco=endereco)

    clientes.append(cliente)
    

def lista_contas(contas):
    print(contas)
    for conta in contas:
        print("="*10)
        print(contas)

def exibir_extrato(clientes):
    cpf = input("qual o cpf? ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("não encontrou cliente")
        return
    
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    print("============extrato============")
    transacoes = conta.historico.transacoes

    extrato = ""
    if not transacoes:
        extrato = "não tem histórico de transação"
    else:
        for transacao in transacoes:
            extrato += f"{transacao['tipo']}: R$ {transacao['valor']:.2f}"
    
    print(extrato)
    print(f"Saldo: R$ {conta.saldo:.2f}")



while True:
    valor = input(menu)
    if valor == "D":
        print("\n \n==============depositar==============")   
        depositar(usuarios) 
        
        
    elif valor == "S":
        print("\n \n==============Sacar==============")          
        sacar(usuarios)
       
       
    elif valor == "E":
        exibir_extrato(usuarios)
    elif valor == "NU":
        print("\n \n==============Novo usuario==============")
        criar_cliente(usuarios)

    elif valor == "NC": #nova conta
       numero_conta = len(contas)+1
       print("contas = " + str(contas))
       criar_conta(numero_conta, usuarios, contas) 
       
    elif valor == "LC":
        print("\n \n==============Listar conta==============")
        print("listando contas criadas...")
        lista_contas(contas)
    elif valor == "Q":
        break
    else:
        print("Valor invalido, seleciona uma opção válida!")
    




