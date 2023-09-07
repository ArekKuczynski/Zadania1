import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from length import number_length


def get_length(num):
    return int(len(str(num)))

def test_number_length_1():
    assert number_length("1") == get_length("1")
    
def test_number_length_2():
    assert number_length("867") == get_length("786")

def test_number_length_3():
    assert number_length("-1") == get_length("-1")

def test_number_length_4():
    assert number_length("a") == "Błąd"