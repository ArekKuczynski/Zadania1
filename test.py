from length import number_length

def get_length(num):
    return len(str(num))

def test_number_length_1():
    assert number_length(1) == get_length(1)