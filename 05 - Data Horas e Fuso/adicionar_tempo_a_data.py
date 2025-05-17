import datetime

data_hora = datetime.datetime(2024,4,18,11,11,11,11)#criando data e hora

print(data_hora)


data_hora += datetime.timedelta(weeks=1) #adicionando uma semana a minha data_hora

print(data_hora)







data_hora = datetime.datetime(2024,4,18,11,11,11,11)#criando data e hora

horas = data_hora.time()#forma de pegar horas da data
print(horas)