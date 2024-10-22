spam = ['cat','cat', 'bat', 'rat','elephant']
print(spam[0])
print(spam[-2])
spam[2]="rate"
print(spam)
spam.append("horse")
print(spam)
spam.insert(3,"big")
print(spam)
del spam[2]
print(spam)
word= spam.pop(3)
print(word)
spam.remove("cat")
print(spam)
spam.sort()
print(spam)
spam.reverse()
print(spam)
print(len(spam))
print(spam)
for spams in spam:
    print(spams.upper())
spam2=spam
print(spam2)
