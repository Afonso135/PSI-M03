 #programa para validar uma expressão matemática em relação ao parênteses curvos e retos
def Validação(expressão):
    expressão=input("insira uma expressão matemática")
    contar_parênteses=0
    contar_parênteses2=contar_parênteses-1
    for l in expressão:
      if contar_parênteses2!=0:
       return False
      else:
       return True
     
Validação("(2+4)*(2+2)")

     
 