contatos = {
    "email1g@gmail.com":{"nome": "nome 1", "Telefone":"1111111"}
    , "email2g@gmail.com":{"nome": "nome 2", "Telefone":"2222222"}
    , "email3g@gmail.com":{"nome": "nome 3", "Telefone":"3333333"}
    , "email4g@gmail.com":{"nome": "nome 4", "Telefone":"4444444"}
    , "email5g@gmail.com":{"nome": "nome 5", "Telefone":"5555555"}
}


#remove a chave do dicionario
del contatos["email5g@gmail.com"]


#remove a chave do subdicionario
del contatos["email1g@gmail.com"]["Telefone"]