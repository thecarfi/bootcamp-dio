conjunto_1 = {1,2,3,4}
conjunto_2 = {9,8,7,6,1,2,3,4}
conjunto_3 = {11,12,13,0}



conjunto_1_nao_esta_em_2 = conjunto_1.isdisjoint(conjunto_2)

conjunto_3_nao_esta_em_2 = conjunto_3.isdisjoint(conjunto_2)


print("O conjunto 1 NÃO esta dentro do conjunto 2? " + str(conjunto_1_nao_esta_em_2))

print("O conjunto 3 NÃO  esta dentro do conjunto 2? " + str(conjunto_3_nao_esta_em_2))