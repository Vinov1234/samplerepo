print('hello there!\nhow are you?\ni\' m doing  fine')
print(r' mthat is carol\'s cat.')# a raw string completey all escape character
print('''Dear Alice,

Eve's cat has been arrested for catnapping, cat burglary, and extortion.

Sincerely
,
bob''')#multiple string with triple qutoes
def spam():
    """This is a multiline comment to help
    explain what the spam() function does."""
    print('Hello!')


name ='1a'
age ='20000'
print('hello, my  name is    ' + name +   ' i am '+str(age) + 'years old')
print('my name is %s i am %s years old' %(name,age))#string interpolation
print(f'my name is{name } next year i will be {age+1}')


print('How are you?')
feeling = input()
if feeling.lower() == 'great':
    print('I feel great too.')
else:
    print('I hope the rest of your day is good.')
