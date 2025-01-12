def FizzBuzz(up_To):
    for i in range(1,up_To+1 ):
        if i%3==0 and i%5==0:
            print("FizzBuzz","end")
        if i%3==0 and i%5!=0:
            print("Fizz","end")
        if i%3!=0 and i%5==0:
            print("Buzz","end")
        else:
            print(i)


FizzBuzz(123456)
