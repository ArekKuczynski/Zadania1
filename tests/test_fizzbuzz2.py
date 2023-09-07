import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from fizzbuzz2 import fizzbuzz

def get():
    list_1 = []
    for i in range(1,101):
        if i % 3 == 0 and i % 5 == 0:
            list_1.append('FizzBuzz')
        elif i % 3 == 0:
            list_1.append('Fizz')
        elif i % 5 == 0:
            list_1.append('Buzz')
        else:
            list_1.append(i) 
    return list_1

def test_fizzbuzz_1():
    assert fizzbuzz([i for i in range(1,101)]) == get()


    

    
