contatos = {
    "email1g@gmail.com":{"nome": "nome 1", "Telefone":"1111111"}
}


print(contatos)

#adiciona a chave um novo valor
contatos.update({"email1g@gmail.com":{"nome":"valor1"}})

#caso a chave não exista no dicinoario, ela será criada
contatos.update({"teste":{"Chave1":"valor1"}})

print(contatos)



teste = {"chave":"valor","chave2":"valor2"}


print(teste)

teste.update({"chave":"234"})

print(teste)