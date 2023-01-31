#%%
#MODULE STRUCTURE
#It is used to store the functions, classes, dictionaries, lists and sets an etc. that be used in another external file 

def add(num1, num2 ):
    print(num1 + num2)
def substract(num1, num2):
    print(num1 - num2)
def divide(num1, num2 ):
    print(num1 / num2)
def multiply(num1, num2):
    print(num1 * num2)    
    
#Now I will create a new file called "CallModule" and call these functions from an external file.

customer = {"firstName" : "Engin", 
            "lastName" : "Banzaroğlu"}