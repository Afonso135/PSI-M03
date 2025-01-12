def FizzBuzz_v2(up_To):
    for i in range(1,up_To+1 ):
        if i%15==0:
            print("FizzBuzz","end")
        if i%3==0 and i%5!=0:
            print("Fizz","end")
        if i%3!=0 and i%5==0:
            print("Buzz","end")
        else:
            print(i)


FizzBuzz_v2(123456)

def FizzBuzz_v3(up_To):
    for i in range(1,up_To+1 ):
        print("FizzBuzz") if i%15==0 else "Fizz" if i%3==0 ("Buzz") else i%5==0 (str(i),end="")