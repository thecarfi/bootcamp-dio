class cachorro():
    def __init__(self, nome,cor, acordado=True): #inicializando o contrutor
        print("inicializando construtor")
        self.nome = nome
        self.cor = cor
        self.acordado  = acordado
    
    def __del__ (self): # primeira forma de destruir o construtor
        print("removendo construtor")


    def latir(self):
        print('latindo...')

c = cachorro("nome Cachorro", "amarelo")
#del c # segundo forma de destruir um construtor
c.latir() 
