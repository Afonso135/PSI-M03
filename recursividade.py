def contar(n):
    if n==100:
        return n
    contar(n+1)

    contar(10)

    print(contar(10))