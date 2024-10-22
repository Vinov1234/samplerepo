import pyinputplus as pyip
response =  pyip.inputNum('enter num:', min =4)
print(response)

response1 = pyip.inputNum('Enter num: ', greaterThan=4)
print(response1)

response2 = pyip.inputNum('>', min=4, lessThan=6)
print(response2)
