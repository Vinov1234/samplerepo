import pprint
message = 'it was a bright cold day in apirl,and the clocks were striking thriten '
count = {}
for charcter in message:
    count.setdefault(charcter,0)
    count[charcter] = count[charcter] +1
    print(count)
pprint.pprint(count)    
    
