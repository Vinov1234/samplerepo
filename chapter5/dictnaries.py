eggs ={'name':'zophie','species': 'cat', 'age': '8'}
ham = {'species': 'cat','age': '8', 'name': 'zopie'}
print(eggs == ham)
mycat ={'size': 'fat', 'color':'grey','disposition':'loud'}
print('my cat has ' + mycat['color']  +  ' fur')

birthdays = {'Alice':'apr 1', 'bob': 'dec 12', 'carol':'mar 4'}

while True:
    print('enter a name :(blank to quit)')
    name = input()
    if name == '':
        brak
    if name in birthdays:
        print(birthdays[name] + 'is the birthday of ' + name)
    else:
        print('i do not have birthday information for ' + name)
        print('what is their birthday?')
        bday = input()
        birthdays[name] = bday
        print('Birthday database updated')
spam = {'name': 'zophie','age':7}
print(name.spam.keys())
