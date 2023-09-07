def area_of_country(country, land):
    try:
        country = str(country)
        if country.isalpha() == True:
            try:
                land = int(land)
                
                total = 148940000
    
                num = round(float(land)/float(total)*100,2)
                
                return f"{country} is {num}% of the total world's landmass"
                
            except:
                return "Ma być int"
        else:
            raise Exception
    except:
        return "Ma być string"