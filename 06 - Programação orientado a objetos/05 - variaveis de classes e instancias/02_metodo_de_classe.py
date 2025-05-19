class pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade =  idade

    @classmethod #aqui permite que eu instancia a função sem precisar instanciar a função pai
    def criar_apartir_data_nasc(cls, ano, mes, dia, nome):
        print(cls)
        idade = 2025 - ano
        return cls(nome, idade)
    

    @staticmethod #aqui é o segundo jeito de eu instanciar a função sem precisar instanciar a função pai
    def eh_maior_idade(idade):
        return idade >= 18


# p = pessoa("henrique",25)

# print(p.nome,p.idade )

p2 = pessoa.criar_apartir_data_nasc(2000, 4,18, "henrique")
print(p2.nome, p2.idade)

print(pessoa.eh_maior_idade(19))
print(pessoa.eh_maior_idade(17))