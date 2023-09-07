def stutter(word):
    try:
        if len(word) < 2:
            raise Exception
        for i in word:
            if ord(i) < 97 or ord(i) > 123:
                raise Exception
        
        return word[:2]+"... "+word[:2]+"... "+word+"?"
    except:
        return "Błąd"