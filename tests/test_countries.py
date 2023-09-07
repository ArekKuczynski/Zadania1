import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from countries import area_of_country

def get_country(str1, num1):
    return f"{str1} is {round(float(num1)/float(148940000)*100,2)}% of the total world's landmass"

def test_country_1():
    assert area_of_country("Poland", 99999) == get_country("Poland", 99999)

def test_country_2():
    assert area_of_country("Poland", "Germany") == "Ma być int"

def test_country_3():
    assert area_of_country(2, "Germany") == "Ma być string"

    
