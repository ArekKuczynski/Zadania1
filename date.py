def format_date(date_old):
    try:
        
        if len(date_old) != 10:
            raise Exception
        if date_old[2] != "/" or date_old[5] != "/":
            raise Exception
        
        date_new = date_old[6:]+date_old[3:5]+date_old[:2]
        return date_new
        
    except:
        return "Podaj date w dobyrym formacie"
    
    

