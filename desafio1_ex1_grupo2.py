"""
desenvolva um função que recebeu uma string e devolve verdadeiro se todas as letras da stringe são iguais 
ou falso nos restantes casos
"""
def letras(texto):
    for letra in texto:
        if letra!=texto[0]:
            return False
    return True

