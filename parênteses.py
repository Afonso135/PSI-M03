
def Validação(expressão):
    expressão=input("insira uma expressão matemática")
    contar_parênteses=0
    for i in  expressão :
     x=False
     y=True
     validação=contar_parênteses%2
     if validação!=0:
       return x
    else:
     return y
    

 