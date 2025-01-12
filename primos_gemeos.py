"""
2 nº primos gémeos são dois nº primos que se distaciam entre 2 unidades
Fazer um prograam que lê 2 nº e inteiros positivos  e diz se são primos e primos gémeos
"""
from primo import primo
x=int(input("insira um nº"))
y=int(input("insira um nº"))
n_primo=True
nn_primo=False
diferença=x-y
if x%2!=0 and abs(diferença)==2:
 print("Os nº são primos e gémeos")
else:
 print("os valores são primos")
 