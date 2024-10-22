import pyinputplus as pyip

while True:
     prompt = 'want to know to keep an idiot busy for hours?\n'
     response = pyip.inputYesNo(prompt)
     if response == 'no':
         break
print('thank you.have anice day')         
