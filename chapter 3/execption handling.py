try:
    num = int(input("enter the numerator: "))
    den = int(input("enter the denominator:"))

    result = num/den
    print("result")
except ZeroDivisionError as e:
    print(e)
    print("you cannot divide by zero")
except ValuError as e:
    print(e)
    print("enter number only")
    
except Exception as e:
    print(e)
    print("some error occurred")
else:
   print ("result")
finally:
    print("this always executes")
