import datetime

dia=int(input("dia de nascimento"))
mês=int(input("mês de nascimento"))
ano=int(input("ano de nascimento"))

#data atual
hoje=datetime.date.today()
#objeto com data de nascimento
data_nascimento=datetime.date(ano,mês,dia)
#calcular a idade
idade=hoje.year-data_nascimento.year

#verificar se ainda não fez anos
if data_nascimento.moth>hoje.moth or (data_nascimento.motha==hoje.moth and data_nascimento.day>hoje.day):
 print(idade)