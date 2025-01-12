"""
escreva uma função que recebe três valores e devolve o maior se todos os números são posivitivos
ou devolve o menor se forem todos negativos, e nas situações restantes devolve none
"""

def coparação(n1,n2,n3):
 # maior
 if n1>n2:
  maior=n1
 else:
  maior=n2
  if n3>maior:
   maior=n3
#menor
 if n1<n2:
  menor=n1
 else:
    menor=n2
 if n3<menor:
  menor=n3
  if n1>0 and n2>0 and n3>0:
   return maior
  if n1>0 and n2>0 and n3>0:
   return menor
  else:
   return None


