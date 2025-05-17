conjunto = {1,2,3,4,5}

print(conjunto)

#O discard() remove determinado valor sem dar erro caso ele não exista
conjunto.discard(1) #se o valor a ser discartado existe, é removido

conjunto.discard(0)# se o valor a ser discartado não existir, fica numa boa. Não da erro

print(conjunto)


#O remove() remove registros apresentando erro, caso esse não exista
conjunto.remove(2)