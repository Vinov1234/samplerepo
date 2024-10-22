import pyinputplus as pyip
import random,time

numberofqustions = 10
correctanswers  = 0
for qustionnumber in range (numberofqustions):
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)
    prompt = '#%s: %s  x %s = ' %(qustionnumber, num1,num2)
    try:
        pyip.inputStr(prompt, allowRegexes=['^%s$' %(num1*num2)],blockRegexes=[('.*','incorrect!')],timeout=8,limit=3)
        
    except pyip.TimeoutException:
        print('out of timt!')
    except pyip.RetryLimitException:
        print('out of tries')
    else:
        print('correct!')
