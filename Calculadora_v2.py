"""
programa para implementar uma calculadoraaa simples utilizando funções
"""
def Soma():
 x=float(input("insira um número"))
 y=float(input("insira um número"))
def Subtrair():
 x=float(input("insira um número"))
 y=float(input("insira um número"))
 print(x+y)
def Subtração():
  x=float(input("insira um número"))
  y=float(input("insira um número"))
  print(x-y)
def Divisão():
 x=float(input("insira um número"))
 y=float(input("insira um número"))
 print(x/y)
def Multiplicação():
 x=float(input("insira um número"))
 y=float(input("insira um número"))
 print(x*y) 
def menu():
 """""
Mostra ao utilizador as operações disponiveis
"""
print("1-Somar/2-Subtrair/3-Divisão/4-Multiplicação/5-Terminar")
OP=input("insira a operação a realizar")
while OP!=5:
   print("1-Somar/2-Subtrair/3-Divisão/4-Multiplicação/5-Terminar")
   OP=input("insira a operação a realizar")
if OP=="1":
 Soma()
 if OP=="2":
   Subtração()
elif OP=="3":
 Divisão()
else:
 Multiplicação()

def main():
    menu()

if __name__=="__main__":
    main()