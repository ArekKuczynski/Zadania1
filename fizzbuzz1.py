def fizzbuzz():
    for i in range(1,101):
        if i in [i for i in range(1,101) if i%3==0] and i in [i for i in range(1,101) if i%5==0]:   print("FizzBuzz")  
        elif i in [i for i in range(1,101) if i%3==0]:  print("Fizz")   
        elif i in [i for i in range(1,101) if i%5==0]:  print("Buzz")  
        else:   print(i)
fizzbuzz()