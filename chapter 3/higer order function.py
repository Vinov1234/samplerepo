def happy():
    print('jummpping')

def sad():
    print("crying")

def calmdown():
    print("calm down")
''' joy = happy
joy()
sorrow = sad
sorrow '''
def feeling(func):
    return calmdown
    func()
func = feeling(happy)
func()
func2 = feeling(sad)
func2()
