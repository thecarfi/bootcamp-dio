#o comando set() remove os valores duplicados de uma lista (não necessariamente ficará na mesma ordem)



lista = ["valor 1","valor 1","valor 2", "valor 3"]

print(set(lista))

print(set ("abacaxi")) #remove as letras repetidas

#não é possivel consultar o resultado no set() direto sem antes converter para uma nova lista

textos = set("abacaxi")
for texto in textos:
    print(texto)