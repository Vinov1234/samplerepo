import pyinputplus as pyip
response = pyip.inputNum(allowRegexes=[r'(I|V|X|L|C|D|M)+', r'zero'])
print(response)


response1 = pyip.inputNum(allowRegexes=[r'(i|v|x|l|c|d|m)+', r'zero'])
print( response1)

response2 = pyip.inputNum(blockRegexes=[r'[02468]$'])
print(response2)


response = pyip.inputStr(allowRegexes=[r'caterpillar', 'category'],
blockRegexes=[r'cat'])
