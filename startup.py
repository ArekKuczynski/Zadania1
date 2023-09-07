def start(x):
    if x == "1":
        from length import number_length
        num = input("Podaj liczbę: ")
        print(number_length(num))
        
    elif x == "2":
        from countries import area_of_country
        str1 = input("Podaj kraj: ")
        num1 = input("Podaj powierzchnie: ")   
        print(area_of_country(str1,num1))
        
    elif x == "3":
        from circle import circle_or_square
        radius = input("Podaj promień okręgu: ")
        area = input("Podaj pole kwadratu: ")
        print(circle_or_square(radius,area))
        
    elif x == "4":
        from highest_int import find_highest
        def panel():    
            print("Podaj kolejno wartości listy, gdy skonczysz wpisz end: ")

            list1 = []
            while True:
                num = input("Podaj liczbe: ")
                
                if num == "end":
                    break
                else:
                    try:
                        test = int(num)
                        list1.append(num)
                    except:
                        print("Błąd podaj liczbe")
                        
                
            print("Oto lista:",list1)
            print("Najwyższa wartość:",find_highest(list1))

        panel()
        
    elif x == "5":
        from date import format_date
        date_old = input("Podaj date w fomracie 'MM/DD/YYYY': ")
        print(format_date(date_old))

    elif x == "6":
        from stuttering import stutter
        word = input("Podaj wyraz o dlugosci conajmniej 2 i taki ktory ma tylko małe litery: ")
        print(stutter(word))
    
    elif x == "7":
        from date import format_date
        date_old = input("Podaj date w fomracie 'MM/DD/YYYY': ")
        print(format_date(date_old))
    
    elif x == "85":
        from date import format_date
        date_old = input("Podaj date w fomracie 'MM/DD/YYYY': ")
        print(format_date(date_old))
    
    elif x == "9":
        from date import format_date
        date_old = input("Podaj date w fomracie 'MM/DD/YYYY': ")
        print(format_date(date_old))
print("Który program?: ",end="\n\n")
print("1. Length")
print("2. Countries")
print("3. Circle vs square")
print("4. Highest_int")
print("5. Date")
print("6. Stuttering")
print("7. Fizzbuzz 1")
print("8. Fizzbuzz 2")
print("9. Fizzbuzz 3",end="\n\n")

decision = input("Podaj numer: ")
start(decision)