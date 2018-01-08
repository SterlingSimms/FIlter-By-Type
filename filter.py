def differentTypes(a):
    #if type(a) == int:
    if isinstance(a, int):
        if a >= 100:
            print "That's a big number!"
        if a < 100:
            print "That's a small number"
    if isinstance(a, str):
    #if type(a) == str:
        if len(a) >=50:
            print "Long sentence"
        if len(a) <50:
            print "Short sentence"
    if isinstance(a, list):
    #if type(a) == list:
        if len(a) >=10:
            print "Big list"
        if len(a) <10:
            print "Short list"
differentTypes()



