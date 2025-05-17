contatos = {
    "email1g@gmail.com":{"nome": "nome 1", "Telefone":"1111111"}
    , "email2g@gmail.com":{"nome": "nome 2", "Telefone":"2222222"}
    , "email3g@gmail.com":{"nome": "nome 3", "Telefone":"3333333"}
    , "email4g@gmail.com":{"nome": "nome 4", "Telefone":"4444444"}
    , "email5g@gmail.com":{"nome": "nome 5", "Telefone":"5555555"}
}





#verificando se a chave "email1g@gmail.com" existe no dicionario contatos
print("email1g@gmail.com" in contatos)


#Verificando se a chave "nome" existe dentro do dicionario do valor da chave "email1g@gmail.com"
print("nome" in contatos["email1g@gmail.com"])