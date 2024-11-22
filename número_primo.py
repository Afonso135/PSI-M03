# função que recebe um número e mostra verdadeiro se for primo ou falso se não for
def primo(n):
    n_primo=True
    for i in range (2,n):
        if n%i==0:
            nn_primo=False
            break
    return

if primo(5)==True:
    print("o nº 5 é primo")
else:
    print("o nº 5 não é primo")







