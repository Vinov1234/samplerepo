f = open("fruits.txt" ,"a")
f.write("apple\n")
f.write("banana")
f.close()
'''content = f.read()
print(content)

f.write("banana")'''

f = open("fruits.txt","r+")
print(f.readline())
