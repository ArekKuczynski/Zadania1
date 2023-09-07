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