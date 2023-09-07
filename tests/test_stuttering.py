import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from stuttering import stutter

def test_stutter_1():
    assert stutter("pytest") == "py... py... pytest?"

def test_stutter_2():
    assert stutter("p") == "Błąd"

def test_stutter_3():
    assert stutter("PYTEST") == "Błąd"

    

    
