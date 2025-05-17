#para criar um dicionario, usa-se as chaves {chave:valor} ou o comando dict(chave:valor)



pessoa ={"nome": "henrique", "idade": 28}
#o metodo da linha de cima e da de baixo produzem o mesmo resultado
pessoa = dict(nome="Henrique",idade=28)

print(pessoa)

# o método abaixo pressupõe que o dicionario PESSOA 
# ja existe e esta adicinando apenas novas chave:valor
pessoa["contato"] = "1234-5678"


print(pessoa)#lista o dicionario

print(pessoa["nome"])#lista valor de uma chave do dicionario


pessoa["nome"] = "novo valor para a chave nome"

