import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from date import format_date

def test_date_1():
    assert format_date("07/09/2023") == "20230907"

def test_date_2():
    assert format_date("11/12/2019") == "20191211"

def test_date_3():
    assert format_date("12/31/2019") == "20193112"

def test_date_4():
    assert format_date("01/15/2019") == "20191501"

def test_date_5():
    assert format_date("01152019") == "Podaj date w dobyrym formacie"

def test_date_5():
    assert format_date("01/15/20199") == "Podaj date w dobyrym formacie"
    

    
