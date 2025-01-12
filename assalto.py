#função para ler o dinheiro do assalto 
def Dinheiro():
    dinheiro_roubado=float(input("insira  a quantidade de dinheiro roubado"))
    while dinheiro_roubado<=0:
        dinheiro_roubado=float(input("insira  a quantidade de dinheiro roubado"))
       

# função para calcular e mostrar o que cada um recebe
def lucro(dinheiro_roubado):
    dinheiro_líder=dinheiro_roubado/2
    dinheiro_brutamontes=dinheiro_líder/4
    dinheiro_condutor=dinheiro_brutamontes/2
    print("O lider vai receber"(dinheiro_líder.round(2))"€")
    print("Os brutamontes vão receber"(dinheiro_brutamontes.round(2))"€")
    print("O condutor vai recber"(dinheiro_condutor.round(2))"€")

_
    """
    função para calcular e rdetornar o valor de juros que cada um paga por mês
    e os juros acumulados ao longo de 10 anos.
    """

def juros_década(dinheiro_líder,dinheiro_brutamontes,dinheiro_condutor):
   juros_líder=dinheiro_líder*0.05
   juros_líder_década=juros_líder*10
   juros_brutamontes=dinheiro_brutamontes*0.05
   juros_brutamontes_década=juros_brutamontes*10
   juros_condutor=dinheiro_condutor*0.05
   juros_condutor_década=juros_condutor*10


def duração(juros_líder,juros_brutamontes,juros_condutor):
   valor_mês



def main():
    if __name__==__main__:
     main()

