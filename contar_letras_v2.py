def contar_letras(letra,frase):
    contar=0
    for i in frase:
        if i==letra:
            contar=contar+1
    return contar