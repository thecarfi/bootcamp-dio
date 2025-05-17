contatos = {
    "email1g@gmail.com":{"nome": "nome 1", "Telefone":"1111111"}
    , "email2g@gmail.com":{"nome": "nome 2", "Telefone":"2222222"}
    , "email3g@gmail.com":{"nome": "nome 3", "Telefone":"3333333"}
    , "email4g@gmail.com":{"nome": "nome 4", "Telefone":"4444444"}
    , "email5g@gmail.com":{"nome": "nome 5", "Telefone":"5555555"}
}


#caso printe o comando pop, ele vai listar a chave que esta removendo
print(contatos.pop("email1g@gmail.com")) 


#Caso passe o segundo argumento, retorna ele se o primeiro não for encontrado
print(contatos.pop("email1g@gmail.com","Não encontrou a chave")) 

print(contatos)