#this is a method we apply when an error occured.

num = int(input("Enter a number")) # what if the user enters char?


try : 
    number = int(input("Enter a number"))
except ValueError : #type of the error is declared 
    print("ValueError Occured.") 
except ZeroDivisionError : #type of error when the denominator is zero in divison operator.
    print("Denominator cannot be zero")
except : #It runs everytime an any error occurs. Type of error didn't declared.
    print("Error Occured. Invalid value.") # If an error occures, the programme will not shut down. Instead, it will print this.
finally :
    print("This block runs either try block or except block. It is independent.")

