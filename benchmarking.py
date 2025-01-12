import math
def função_complicada():
    for i in range(1000000):
        _=i**2
#Calcula a exponenciação utilizando a função pow do módulo math
def função_complicada2():
    for i in range(1000000):
        _=math.pow(i,2)

import datetime
def medir_time():
    inicio=datetime.now()
    função_complicada2()
    fim=datetime.now()
    tempo_execução=fim-inicio
    print(tempo_execução)
    
    
medir_time()