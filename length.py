def number_length(num):
    dlugosc = 0
    for i in num:
        dlugosc += 1
                
    print(dlugosc)

while True:
    try:
        num = input("Podaj liczbę: ")
            
        num = int(num)
        num = str(num)
            
        number_length(num)
            
        break
    except:
        print("Błąd")