def fizzbuzz():
    list1 = []
    for i in range(1,101):
        try:
            test = i / (i%3) #kiedy zero to blad
            test = i / (i%5)
            list1.append(i)
        except:
            try:
                test = i / (i%3)
                list1.append("Buzz")
            except:
                try:
                    test = i / (i%5)
                    list1.append("Fizz")
                except:
                    list1.append("FizzBuzz")
    return list1