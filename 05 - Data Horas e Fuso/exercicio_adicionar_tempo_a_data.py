import datetime




tipo_carro = 'p'#p,m,g
tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60
data_atual = datetime.datetime.today() #o noew() é a zona atual

if tipo_carro == 'p':
    data_estima = data_atual + datetime.timedelta(minutes=tempo_pequeno)
    print(f"O carro chegou as {data_atual} e ficará pronto as {data_estima}")

elif tipo_carro == 'm':
    data_estima = data_atual + datetime.timedelta(minutes=tempo_medio)
    print("é carro medio")

elif tipo_carro == 'g':
    data_estima = data_atual + datetime.timedelta(minutes=tempo_grande)
    print("é carro grande")


 