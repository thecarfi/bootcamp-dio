conjunto_1 = {1,2,3,4}
conjunto_2 = {9,8,7,6,4,3,2}


#só apresenta os valores que não se repete entre os conjuntos
diferenca = conjunto_1.symmetric_difference(conjunto_2)


print(diferenca)