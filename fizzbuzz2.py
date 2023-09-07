def fizzbuzz(loop,indx=0):
    if loop[indx] % 3 == 0 and loop[indx] % 5 == 0:
        loop[indx] = "FizzBuzz"
    elif loop[indx] % 3 == 0:
        loop[indx] = "Fizz"
    elif loop[indx] % 5 == 0:
        loop[indx] = "Buzz"
    
    indx = indx+1
    if indx==100:
        return loop
    else:
        return fizzbuzz(loop,indx)
print(fizzbuzz([i for i in range(1,101)]))