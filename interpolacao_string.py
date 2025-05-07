nome = "Henrique"
idade = 25
profissao = "Analista de dados"
linguagem = "Python"

######################################
#esse método não é recomendado
print("teste 1 - Nome: %s, idade: %d" % (nome,idade))

######################################
#esse método não é recomendado
print("teste 2 - Nome: {}, idade: {}".format(nome,idade))

######################################
#esse método não é recomendado
print("teste 3 - Nome: {0}, idade: {1}".format(nome,idade))

######################################
#esse método não é recomendado
print("teste 4 - Nome: {nome}, idade: {idade}".format(nome=nome,idade=idade))


######################################
#esse método não é recomendado

dados = {"nome": "Henrique", "idade": 25}

print("teste 5 - nome: {nome}, idade: {idade}".format(**dados))

######################################
print(f"teste 6 - Nome: {nome}, idade: {idade}")