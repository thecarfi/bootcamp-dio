import datetime


data_hora = datetime.datetime.today()

print(data_hora)


data_texto = data_hora.strftime("%d/%m/%y")#extraindo a data (se atentar para o case sensitive da mascara)

data_hora_texto = data_hora.strftime("%d/%m/%y %H:%M:%S") #extraindo a data e hora (se atentar para o case sensitive da mascara)

horas_texto = data_hora.strftime("%H:%M:%S") #extraindo as horas (se atentar para o case sensitive da mascara)

print("A data e horas são: " + data_hora_texto)

print("A data é: " + data_texto)

print("As horas são: " + horas_texto)
##############################################################


data_em_formato_data = datetime.datetime.strptime(data_texto, "%d/%m/%y")#se atentar para o case sensitive da mascara

print(data_em_formato_data)