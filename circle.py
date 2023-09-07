import math

def circle_or_square(radius, area):
    circle = 2 * round(math.pi,2) * float(radius)
    square = math.sqrt(float(area)) * 4
    
    if circle > square:
        return True
    else:
        return False

try:
    
    radius = input("Podaj promień okręgu: ")
    area = input("Podaj pole kwadratu: ")
    
    radius = float(radius)
    area = float(area)
    
    print(circle_or_square(radius,area))
except:
    print("Błąd podaj liczby")