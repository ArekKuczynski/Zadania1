import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from circle import circle_or_square

def get_circle_or_square(num1, num2):
    return 

def test_circle_1():
    assert circle_or_square(16, 625) == True
    
def test_circle_2():
    assert circle_or_square(5, 100) == False
    
def test_circle_3():
    assert circle_or_square(8, 144) == True
    
def test_circle_4():
    assert circle_or_square(14, 500) == False

def test_circle_5():
    assert circle_or_square("a", 500) == "Błąd podaj liczby"

def test_circle_5():
    assert circle_or_square(500, "b") == "Błąd podaj liczby"
    
