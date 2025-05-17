contatos = {
    "email1g@gmail.com":{"nome": "nome 1", "Telefone":"1111111"}
    , "email2g@gmail.com":{"nome": "nome 2", "Telefone":"2222222"}
    , "email3g@gmail.com":{"nome": "nome 3", "Telefone":"3333333"}
    , "email4g@gmail.com":{"nome": "nome 4", "Telefone":"4444444"}
    , "email5g@gmail.com":{"nome": "nome 5", "Telefone":"5555555"}
}



contatos_2 =contatos.copy()#copiando dicionario

contatos_2["email1g@gmail.com"] = {"chave1":"valor"}

print(contatos_2["email1g@gmail.com"])
print(contatos["email1g@gmail.com"])
