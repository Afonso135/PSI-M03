# programa/função que encontra o máximo divisor de um número
def MDC(x,y):
    menor=x
    for i in range(x,y):
        if y<menor:
            maior_divisivor=None
        for i in range(2,menor):
            if x%i==0 and x%i==0:
                maior_divisivor=i
                return maior_divisivor