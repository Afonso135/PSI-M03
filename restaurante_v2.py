# menu
def menu():  
 print("1.Entrada/2.Estado/3.Saída/4.Terminar")

  
#função para resgistar os clientes que entram e as mesas que são cupadas
def entrada():
    while lim_mesas or lim_clientes>0:
      clientes_atuais=int(input("insira o nº de clientes que entraram"))
      mesas=int(input("insira o nº de mesas a ocupar"))
      while op!=4: 
          if op==1:
             entrada(clientes_atuais,clientes_atuais):
             if lim_clientes==clientes_atuais:
              print("o restaurante está cheio")
              return 0
              

def saída():
                 if op==3:
                  clientes_saída=int(input("insira o nº de clientes que saíram"))
                  clientes_saída=clientes_saída(clientes_atuais)
                  clientes_atuais=clientes_atuais-clientes_saída
                  custo=float(input("insira o preço de cada refeição"))
                  if mesas==0:
                   return 0
                  print("Todas as mesas estão livres")
                  mesas_saída=int(input("insira o nº de mesas a desocupar"))
                  mesas_desocupadas=mesas_saída(mesas)
                  if clientes_saída>0 or mesas_desocupadas>0:
                    print("quanto gastou a refeição:")
                  return mesas_desocupadas
                 print("o restaurante está cheio") 
# função que regista a saída dos clietes e atualizar o custo total de cada refeição
                 def saíd_2():
                  clientes_saída=int(input("insira o nº de clientes que saíram"))
                  clientes_saída=clientes_saída(clientes)
                  clientes_atuais=clientes_atuais-clientes_saída
                  custo=float(input("insira o preço de cada refeição"))
                  if mesas==0:
                   return 0
                  print("Todas as mesas estão livres")
                 mesas_saída=int(input("insira o nº de mesas a desocupar"))
                 mesas_desocupadas=mesas_saída(mesas)
                 if clientes_saída>0 or mesas_desocupadas>0:
                  print("quanto gastou a refeição:")
                 return mesas_desocupadas

# função que calcula e mostra os dados estatísticos em relação à ocupação do restaurante
def estado_clientes():
  if op==2:
    lugares_livres=lim_clientes-clientes_atuais*100
    return lugares_livres
  mesas_livres=lim_mesas-mesas*100
  return mesas_livres

#nº máximo de clientes que podem estar no restaurante e nº de mesas máximas
lim_mesas=int(input("insira o nº de mesas que tem "))
lim_clientes=int(input("insira o nº de clientes que podem entrar no restaurante"))
op=1
clientes_saída=int(input("insira o nº de clientes que saíram"))
mesas=int(input("insira o nº de mesas a ocupar"))


def main():
  menu()
  if "name"==main:
    main()