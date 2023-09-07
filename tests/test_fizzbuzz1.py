import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from fizzbuzz1 import fizzbuzz

def get():
    for i in range(1,101):
        if i % 3 == 0 and i % 5 == 0:
            print ('FizzBuzz')
        elif i % 3 == 0:
            print ('Fizz')
        elif i % 5 == 0:
            print ('Buzz')
        else:
            print (i) 

def test_fizzbuzz_1():
    assert fizzbuzz() == get()


    

    
