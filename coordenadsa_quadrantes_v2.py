def coordenadas():
    Px=int(input("insira a coodernada do eixo do x"))
    Py=int(input("insira a coodernada do eixo y"))
    if Px==0 or Py==0:
        return("O pponto está sobre os eixos")
    if Px<0 and Py>0:
        return("O ponto está localizado no 1º quadrante")
    if Px<0 and Py>0:
        return("O ponto está localizado no 2º quadrante")
    if Px<0 and Py<0:
        return("O ponto está localizado no 3º quadrante")
    if Px>0 and Py<0:
        return("O ponto está localizado no 4º quadrante")
    


def main():
    coordenadas()
if __name__=="__main__":
    main()