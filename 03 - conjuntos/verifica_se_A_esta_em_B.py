conjunto_1 = {1,2,3,4}
conjunto_2 = {9,8,7,6,1,2,3,4}
conjunto_3 = {1,2,3,0}


#essa função retorna valor verdadeiro ou false se conjunto A esta contido em B

conjunto1_esta_em_conjunto2 = conjunto_1.issubset(conjunto_2)

conjunto3_esta_em_conjunto2  = conjunto_3.issubset(conjunto_2)

print("O conjunto 1 esta em conjunto 2? "+str(conjunto1_esta_em_conjunto2))

print("O conjunto 3 esta em conjunto 2? "+str(conjunto3_esta_em_conjunto2))