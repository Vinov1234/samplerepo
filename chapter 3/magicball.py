import random
def getanswer(answernumber):
    if answernumber == 1:
        return 'it is certain'
    elif answernumber == 2:
        return 'it is decsidly so'
    elif answernumber == 3:
        return 'yes'
    elif answernumber == 4:
        return 'reply hazy try agin'
    elif answernumber == 5:
        return 'ask agin later'
    elif answernumber ==6:
        return 'concenrate try agin'
    elif answernumber == 7:
        return 'my rply is no'
    elif answernumber == 8:
        return'outloo not so good'
    elif answernumber == 9:
        return 'very doubtfull'
        
r = random.randint(1,9)
fortune = getanswer(r)
print(fortune)
