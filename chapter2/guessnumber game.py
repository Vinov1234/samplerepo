import random
secretnumber = random.randint(1,20)
for guessnumber in range(1,7):
    print("take the guess")
    guess = int(input())
    if guess < secretnumber:
        print("your guess is low:")
    elif guess > secretnumber:
        print("youer guess is higer:")
    else:
        break
if guess  == secretnumber:
    print("you done a great job " + str(guessnumber ))
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))
    
    

        
