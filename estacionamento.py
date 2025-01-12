import datetime
def minutos():
 h=int(input("insira hora que entrou no parque"))
min=int(input("insira a que minutos entrou"))
minutos_atuais=datetime.datetime.now().minute
min_parque=minutos_atuais-min

def bloco_15min():
   blocos=min_parque//15
   if min_parque%15!=0:
    blocos+=1


def custo(min_parque):
  preço=float(input("insira o valor que paga a cada 15 minutos"))
  preço_total=blocos*preço
  return preço_total


def main():
  preço=float(input("insira o valor que paga a cada 15 minutos"))
  h=int(input("insira hora que entrou no parque"))
  min=int(input("insira a que minutos entrou"))
#mostrar resultado
print(f"Estacionamento com duração de"(min_parque)"minutos que corresponde a"(blocos)"blocos")