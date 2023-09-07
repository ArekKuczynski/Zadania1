import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from highest_int import find_highest

def get_highest_int(list_1):
    return str(max(list_1))

def test_highest_int_1():
    assert find_highest(["6","5","9","14","2","1","8"]) == get_highest_int([6,5,9,14,2,1,8])

def test_highest_int_2():
    assert find_highest(["6","5","9","14","2","-1","8"]) == get_highest_int([6,5,9,14,2,-1,8])

def test_highest_int_3():
    assert find_highest(["6","5","9","-14","2","1","8"]) == get_highest_int([6,5,9,-14,2,1,8])
    

    
