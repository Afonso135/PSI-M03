alfabeto="abcdefghijklmnopqrstuvwxyz"
alfabeto_cod="bcdefghijklmnopqrstuvwxyza"

def menu():
    texto=input("insira uma mensagem")
    OP=input("insira o que deseja realizar")

def cod(texto):
    """
    função que recdebe uma mensagem E mostra-a codificada com os alfabetos fornecidos
    """
    for l in texto:

        for p in range(len(alfabeto)):
            if l==alfabeto[p]:
                texto=texto+alfabeto_cod[p]
#caso não encontre a letra no abcedário, deve manter a original
    return texto

def descodifica():
    for l in range(len(alfabeto_cod)):
     for p in range(len(alfabeto_cod)):
            if l==alfabeto_cod[p]:
                texto=texto+alfabeto[p]

    



    