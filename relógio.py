from datetime import datetime

while True:
    print(datetime.now())
    #esperar um segundo
    import time
    time.slip(1)

    while True:
        #print(datetime.now())
        hora_atual=datetime.now().strftime("%H:%M:%S")
        print(hora_atual)
        if datetime.now().hour>=16 and datetime.now().minute>=35 and datetime.now().now().second>=0 and despertou==False:
         print("ACORDA!!!")
         despertou=True