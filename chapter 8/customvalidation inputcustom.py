import pyinputplus as pyip
def addsuptoten(numbers):
        numberlist = list(numbers)
        for i, digit in enumarate(numberlist):
            numberlist[i] = int(digit)
        if sum(numberlist) != 10:
            raise Exception('the digit must add up to 10, not %s.'%(sum(numberlist)))
        return int(numbers)
print(response =pyip.inputCustom(addsuptoten))     
