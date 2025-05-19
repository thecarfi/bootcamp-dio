class estudante:
    escola = "DIO" #declarada como variavel de classe (pode ser alterado aplicando os efeitos para todas as instancias)

    def __init__(self,nome,matricula ):
        self.nome = nome #Declarada como variavel de instancia (não da para alterar com uma linha e aplicar para todas as instancia, só aplicando instancia por instancia)
        self.matricula  =matricula #Declarada como variavel de instancia

    def __str__(self):
        return f"{self.nome} -{self.matricula} - {self.escola}"

def mostra_objetos(*objs):
    for   obj in objs:
        print(obj)

aluno_01 = estudante("henrique", 123)
aluno_02 = estudante("henrique2", 321)

print(aluno_01)
print(aluno_02)

aluno_02.matricula = '4444' #atribuindo um novo valor para uma instancia especifica
mostra_objetos(aluno_01)
mostra_objetos(aluno_02)

estudante.escola = "nova escola" #atribuindo um novo valor  a classe inteiro (o impacto é em todas as instancias)

mostra_objetos(aluno_01)
mostra_objetos(aluno_02)

