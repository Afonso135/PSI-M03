import datetime

#data de hoje
print(datetime.date.today)
# ano
print(datetime.date.today().year)
#mês
print(datetime.date.today().mouth)
#data e hora
print(datetime.date.now())
#como srting
print(datetime.datetime.now().strftime("%d-%m"))