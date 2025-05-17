import datetime
#o metodo abaixo é igual ao de cima, sendo o vatagem de importar argumento especifico
#from datetime import date
 

data = datetime.date(2024,4,18)#criando data

print(data)


data_hora = datetime.datetime(2024,4,18,11,11,11,11)#criando data e hora

print(data_hora)

hora = datetime.time(10,2,1,11)#criando hora

print(hora)



data_hora += datetime.timedelta(weeks=1) #adicionando uma semana a minha data_hora

print(data_hora)