import pyinputplus as pyip
response = pyip.inputNum(limit=2)
print(response)

response2 = pyip.inputNum(timeout=10)
print(response2)

response3 = pyip.inputNum(limit=2, default='N/A')
print(response3)
