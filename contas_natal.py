# este programa le o dinheiro gasto e o numero de pessoas, depois devolve o que cada um paga
def natal():
    n_de_pessoas=int(input("insira o número de pesoas"))
    
    for i in range(n_de_pessoas):
        nome=input("insira o seu nome")
        valor=float(input("insira o valor que gastou"))
        total=valor+i  
        return total
    print(nome"gastou"valor"€") 