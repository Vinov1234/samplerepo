
import re
batregex = re.compile(r'bat(wo)?man')
mo1 = batregex.search('the advantures of batman')
print(mo1.group(0))
mo2 = batregex.search(' the adventures of batwoman')
print(mo2.group())

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo1 = phoneRegex.search('My number is 415-555-4242')
print (mo1.group())

mo2 = phoneRegex.search('My number is 555-4242')
print( mo2.group())
