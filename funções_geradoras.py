#for i in range(10):
 #   print(i)
def funçãoA():
    x=x+1
    return x
print(funçãoA)
print(funçãoA)
print(funçãoA)

def funçãoB():
    x=x+1
    while x<10:
     yield x #devolve o valor e mantém o estado

     for i in funçãoB():
        print(funçãoB)