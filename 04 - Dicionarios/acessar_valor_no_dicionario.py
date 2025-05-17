contatos = {
    "email1g@gmail.com":{"nome": "nome 1", "Telefone":"1111111"}
}



contatos.get("chave") #retorna none
print(contatos.get("chave",{"teste"})) #retorna "teste", devido a inserção do {"teste"}

print(contatos.get("email1g@gmail.com"))

print(contatos["email1g@gmail.com"]["nome"])