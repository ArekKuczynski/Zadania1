def number_length(num):
    try: 
        num = int(num)
        num = str(num)
        
        dlugosc = 0
        for i in num:
            dlugosc += 1
                
        return dlugosc

    except:
        return "Błąd"