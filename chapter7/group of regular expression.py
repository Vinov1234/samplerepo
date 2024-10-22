import re
phonenumberregex  = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo =phonenumberregex.search("my number is 415-555-4242.")
print(mo.group(1))
print(mo.group(2))
print(mo.group())

heroregex = re.compile(r'batman |tina fey')
mo1 = heroregex.search('batman and tina fey')
print(mo1.group())

mo1 = heroregex.search("tina fey and batman")
print(mo1.group())


batregex = re.compile(r'bat(man|mobile||copter|bat)')
mo = batregex.search('batmobile last wheel')
print(mo.group())
