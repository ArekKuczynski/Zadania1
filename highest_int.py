def find_highest(list1):

    highest = int(list1[0])
    
    #dla list 1 indexowych jest try
    try:
        if highest < int(list1[1]):
            list1 = list1[1:]
        else:
            del(list1[1])
    except:
        return highest
    
    if len(list1) == 1:
        return list1[0]
    else:
        return find_highest(list1)
    
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