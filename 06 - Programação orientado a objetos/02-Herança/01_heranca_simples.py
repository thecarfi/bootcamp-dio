#Herança simples = quando herda de apenas uma classe

class veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("ligando motor...")
    pass

    def __str__(self): #Permitindo consultar de forma mais clara a classe instanciada (é só printar a instancia, exemplo b1)
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
    
class motocicleta(veiculo):
    pass

class carro(veiculo):
    pass

class caminhao(veiculo):
    def __init__(self,cor, placa, numero_rodas, carregado):
        self.carregado = carregado



    def esta_carregado(self):
        print(f"O caminhão { '' if self.carregado else 'não'} esta carregado")
        print(self.carregado)



moto = motocicleta("azul","abc-123", 2)
moto.ligar_motor()


caminhao = caminhao("vermelho","def-456", 4, False)

caminhao.ligar_motor()

caminhao.esta_carregado()