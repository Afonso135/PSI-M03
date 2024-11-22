import math
#Completa a função de acordo com a docstring
def Area(r):
    if r<0:
     return(None)
    area=math.pi * r**2
    return round(area,2)


#Testes

assert Area(1) == 3.14, "Erro a função devia devolver 3.14"
assert Area(-1) == None, "Erro a função devia devolver None"
assert Area(10) == 314.16, "Erro a função devia devolver 314.16"

print("Função passou nos testes")