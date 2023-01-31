#It makes the code more reusable and changeable instantly.
#%%
city = "İstanbul"

print(city.upper()) # for example upper function is defined already. It can be called and used like this.
print(city.endswith("L")) #it will return TRUE or FALSE. Checks if the given string ends with 'L'
#%%
#functions will be declared with the keyword "def"
def sayHello(name = "Friend"): # If there won't be any arguments passing when calling the function, "Friend" will display as default value.
        #Number of arguments and their default value can be altered.
    print("Hello"+ name) #"Banzar" will be assigned to key "name".
    
sayHello("Banzar") #it calls the function generated before. Sends an argument which will be called as "name" in the function.
sayHello() #It will print "Hello Friend"
#%%
def sayHello2(name = "Dear", surname ="Friend"): # If there won't be any arguments passing when calling the function, "Friend" will display as default value.
        #Number of arguments and their default value can be altered.
    print("Hello"+ "\t" + name + "\t" + surname) #"Banzar" will be assigned to key "name".
sayHello2("Muhammet") #Prints Hello Muhammet Friend
sayHello2("","Banzar") #Assigns name an empty value there for It skips the name and prints Hello Banzar.
#%%
#%%
def sayHello3(name, surname ="Friend") : #There is compulsory arguments which must be stated when calling the function.
        #and there is optinal arguments which is optional. These optionals have to have default value.
        #and these optional arguments need to be in the right most side of the bracelet.
        #(name = "Dear", surname) this format cannot be accepted.      
    print("Hello"+ "\t" + name + "\t" + surname) 
#%%
#FUNCTION THAT RETURNS VALUE---------------------

def dikUcgenAlaniHesapla(a,b):
    return a*b/2

alan = dikUcgenAlaniHesapla(2,3)

print(alan)

#%%
dikUcgenAlaniHesapla2 = lambda a,b : a*b/2
#This is a shorcut for basic return function. It means that I will get 2 arguments from you and I will apply them 
#the operation you asked after colon and return the value.
print(dikUcgenAlaniHesapla2(3,6))

print(type(dikUcgenAlaniHesapla2)) # will print <class 'function'>

x = dikUcgenAlaniHesapla2 # the function is assigned to another word. Therefore x can bu used as the function.

print(x(4,5))
