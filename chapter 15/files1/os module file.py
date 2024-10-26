import os
filename = input("enter file name ")
if os.path.isfile(filename):
    print("yes,present")
    f = open(filename, "r")
    output = f.read()
    print(output)
else:
    print("No,not present")
                 
