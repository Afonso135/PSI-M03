
def menu():
 op=0
 print("1.Gasolina/2.Gasólio/3.Gás/4.Termminar")
 while op !=4:
    depósito=input("insira a quantidade de gasolina que pretende para encher o depósito")

def Estado_gasolina(cap_depósito=float):
  depósito=input("insira a quantidade de gasolina que pretende para encher o depósito")
  cap_atual=cap_depósito-depósito
  percentagem_depósito=cap_atual/100
  return percentagem_depósito

def Estado_gasolina2(cap_atual,percentagem_depósito):
  return cap_atual



  


