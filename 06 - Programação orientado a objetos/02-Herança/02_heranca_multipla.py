
# Herança multipla = quando herda de várias classes


class animal:
    def __init__(self,numero_patas):
        self.numero_patas = numero_patas
    
    def __str__(self): #Permitindo consultar de forma mais clara a classe instanciada (é só printar a instancia, exemplo b1)
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

class mamifero(animal):
    def __init__(self, cor_pelo, **kw):
        self.cor_pelo = cor_pelo
        super().__init__(**kw)


class ave(animal):
    def __init__(self,cor_bico, **kw):
        super().__init__(**kw)
        self.cor_bico = cor_bico


class gato(mamifero):
    pass    

class ornitorrinco(mamifero,ave):
    def __init__(self, cor_bico, cor_pelo,numero_patas ):
        super().__init__(cor_pelo=cor_pelo, cor_bico=cor_bico,numero_patas=numero_patas)

        print(ornitorrinco.__mro__)

##########################
gato = gato(cor_pelo="marrom", numero_patas=4)

print(gato)

##########################

ornitorrinco = ornitorrinco(cor_pelo="preto",numero_patas=2,cor_bico="vermelho")
print(ornitorrinco)
##########################






