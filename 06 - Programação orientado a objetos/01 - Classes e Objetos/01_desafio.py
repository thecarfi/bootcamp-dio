class bicicleta:
    def __init__(self, cor, modelo, ano, valor):    # Abrindo o construtor
        # Abaixo esta incializando os atributos da classe
        self.cor = cor
        self.modelo = modelo
        self.ano = ano 
        self.valor = valor
    
    def buzinar(self):
        print("plim plim...")
    
    def parar(self):
        print("parando...")

    def correr(self):
        print("acelerando...")
    
    def trocar_marcha(self, numero_marcha):
        print("Marcha trocada para: " + str(numero_marcha))
    
    def __str__(self): #Permitindo consultar de forma mais clara a classe instanciada (é só printar a instancia, exemplo b1)
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


b1 = bicicleta("vermelha", "caloi", 2025, 2000.00)

b2 = bicicleta("verde","monark", 2020, 185.00)



print(b2.cor)
b1.correr()
print(b1.cor)

print(b1)
print(b1.trocar_marcha(12))