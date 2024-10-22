#'copy', 'copy2', 'copyfile', 'copyfileobj', 'copymode', 'copystat', 'copytree',
import os
import shutil
f = open("data.txt1",'r')
f1 = open ("data.txt2",'w')
shutil.copyfileobj(f,f1)
f.close()
f1.close()
