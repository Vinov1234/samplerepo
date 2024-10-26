def mobile():
    print("redmi")
    
def moblie2():
    print("moto")
    

def moblie3(fav1):
    fav1()
    print("vivo")
    return moblie2


fav1= moblie3(mobile)
fav1()


