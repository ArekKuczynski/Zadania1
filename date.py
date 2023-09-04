def format_date(date_old):
    date_new = date_old[6:]+date_old[3:5]+date_old[:2]
    return date_new

try:
    date_old = input("Podaj date w fomracie 'MM/DD/YYYY': ")
    if len(date_old) != 10:
        raise Exception
    if date_old[2] != "/" or date_old[5] != "/":
        raise Exception
    
    print(format_date(date_old))
except:
    print("Podaj date w dobyrym formacie")