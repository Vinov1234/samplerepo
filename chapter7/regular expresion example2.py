# ^ $ . * + ? {} \d  all are regular expression
import re
text= "helo world ","goomorint ", "goodnight"
a= re.findall("hell oworld | goodnight",text)
print(a)
