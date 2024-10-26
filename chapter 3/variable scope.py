num =10
def welcome(name):
    global num
    num = 20
    print("welcome " + name)
    print(str(num))
welcome("ratha")    
print("the value of num is:" + str(num))
while  num<= 100:
    print(num)
    num += 10
    
