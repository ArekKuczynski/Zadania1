import math

def circle_or_square(radius, area):
    try:
        
        radius = float(radius)
        area = float(area)
        
        circle = 2 * round(math.pi,2) * float(radius)
        square = math.sqrt(float(area)) * 4
        
        if circle > square:
            return True
        else:
            return False
        
    except:
        return "Błąd podaj liczby"