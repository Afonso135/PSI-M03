def n_inteiro(mensagem="insira um número:"):
#função que lê um número inteiro e garante que é válido
 while True:
  dados=int(input(mensagem))
  if dados[0]=="":
   testar=dados.replace("-","")
  if testar.isdigit():
   return int(dados)
  print("o valor não válido")

def n_inteiro_limites(min,máx=None,mensagem="insira um valor inteiro"):
 while True:
    min=int(input("insira o valor minímo"))
máx=int(input(mensagem))
if dados>=min and (máx is None) or dados<=máx:
  return dadaos


def n_decimal(mensagem=):
"""
função para ler um número decimal. A função garante que o valoré válido e aceita. ou , como separadores de casas decimais
"""
while True:
 dados=int(input(mensagem))
 if len(dados)==0:
    continue
 if dados[0]=="":
   dados=dados.replace("-","")
   #contar os pontos decimais
   pontos=testar.count(".")
   #remover os pontos decimais
testar=dados.replace("_","")

#não pode ter mais que 1 ponto decimal
if testar.isdigit() and pontos<=1:
  return float(dados)
print("o valor não válido")
#substituir virgulas por pontos


def n_decimais_limites(min,max,mensagem="insira um valor"):
  while True:
    valor=n_decimal(mensagem)
    if valor>min and (max is None or valor<=max):
      return valor
    print("o valor não válido")

  