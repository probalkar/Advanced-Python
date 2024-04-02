# exception : events detected during execution that interrupt the flow of program

try:
    num = int(input("Enter numerator: "))
    den = int(input("Enter denominator: "))
    result = num/den
except ZeroDivisionError as e:
    print(e)
    print("You can't divide by 0 idiot!")
except ValueError as e:
    print(e)
    print("Please input numbers only")
except Exception as e:
    print(e)
    print("Something went wrong :(")
else:   # printing result if no errors are encountered
    print(result)
finally:
    print("This finally block is always executed")