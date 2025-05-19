from abc import ABC,abstractmethod

class controle_remoto(ABC):
    @abstractmethod#abstrando o metodo
    def ligar(self):
        pass
    @abstractmethod#abstrando o metodo
    def desligar(self):
        pass

    @property
    @abstractmethod  
    def marca(self):
        pass



class controleTV(controle_remoto):
    def ligar(self):#pelo fato a classe extendida controle_remoto() ter seus metodos abstraidos (ligar() e desligar()), quando eu instancia o controleTV() eu sou obrigado a instanciar a ligar() e desligar()
        print("ligando TV...")
    
    def desligar(self):#instanciando porque a de origem desligar() foi abstraida
        print("desligando TV...")

    def marca(self):
        print("marca 1")

class controle_ar(controle_remoto):
    def ligar(self):#instanciando porque a de origem ligar() foi abstraida
        print("ligando ar condicionado...")
    
    def desligar(self):#instanciando porque a de origem desligar() foi abstraida
        print("desligando ar condicionado...")

    def marca(self):
        print("marca 2")



controle = controleTV()
controle.ligar()
controle.desligar()
controle.marca()


controle2 = controle_ar()
controle2.ligar()
controle2.desligar()
controle2.marca()