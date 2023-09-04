def area_of_country(country, land):
    total = 148940000
    
    num = round(float(land)/float(total)*100,2)
    
    print(country,"is",str(num)+"%","of the total world's landmass")
    

try:
    str1 = input("Podaj kraj: ")
    str1 = str(str1)
    if str1.isalpha() == True:
        try:
            num1 = input("Podaj powierzchnie: ")
            num1 = int(num1)
            
            area_of_country(str1,num1)
            
        except:
            print("Ma być int")
    else:
        raise Exception
except:
    print("Ma być string")