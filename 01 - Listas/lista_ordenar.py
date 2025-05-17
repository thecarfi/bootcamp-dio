lista = ["valor 1", "valor 2", "valor 3 ", "valor 4"]




lista.sort() #ordena a lista em ordem alfabética



lista.sort(reverse=True) #Vai trazer a ordem alfabética reversa


lista.sort(key=lambda x: len(x)) # Ordena de forma crescente pelo tamanho da string

lista.sort(key=lambda x: len(x),reverse=True) # Ordena de forma decrescente pelo tamanho da string


#existe uma função chamada reverse(nome_da_lista,propriedades_aplicadas) que faz a mesma coisa