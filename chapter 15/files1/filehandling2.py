f = open("C:\\Users\pc\\Documents\\fruits.txt" ,"r")
output = f.read(5)
info = "-".join(output)
print(info)
print(f.tell())
f.seek(20)
output = f.read(10)
print(output)
print(f.tell())
f.close()





'''f = open("C:\\Users\pc\\Documents\\fruits.txt" ,"r")
output = f.readlines()
info = " ".join(output)
print(info)
f.close()'''
'''f.write("sathyaraj\n")
f.write("is a\n")
f.write("nice guy") 
list = ["saravan","pradeep","aswin","manikandan","sathayraj"]
f.writelines(list)'''
#print("file is closed or not ",f.close)

'''print("file name is",f.name)
print("file mode is ",f.mode)
print("file property" ,f.readable())
print("file property",f.writable())
print("file is closed or not ", f.closed)'''
