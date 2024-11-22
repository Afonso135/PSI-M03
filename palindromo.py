 # programa que recebe uma stringe e verifica se é um palíndromo
def palindromo(texto):
    palavra=input("insira uma palavra")
    E_palindromo=True
    n_palindromo=False
    palvra_invertida=""
    palavra=palavra.lower()
    for i in range(len(palavra)-1,-1,-1):
        palavra_invertida = palavra_invertida + palavra[i]
    print(palavra_invertida)
    if palavra_invertida == palavra:
        return E_palindromo
    return n_palindromo

    if palindromo("banana")==True:
        print("a palavra não é um palindromo")
    else:
        print("a palavra não É UM Palindromo")
        
