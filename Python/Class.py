#Class structure utilizes the storage of the functions and features of the same subject.
#Helps the organization of the related parameters and functions etc.
#%%
class Math : #first letter is Capital (recommended not necessary)
    def __init__(self):
        print("This is a constructor. This works when you assign them to subjects in line 16, 17 and 18")
    def add(self, num1, num2):#you need to write self left most side of the function. Self refers to class itself
        return num1 + num2
    def substract(self, num1, num2):
        return num1 - num2 
    def multiply(self, num1,num2):
        return num1*num2
    def divide(self, num1, num2):
        return num1/num2

math = Math() #this line means that we created a space in memory about this subject and we can call it with "math"
math2 = Math()
math3 = Math() # you can assign multiple times
print(math.divide(2,8))
#%%
#Property including classes

class Person : 
    def __init__(self, firstName, lastName, age):
        self.firstName = firstName #right side of these equations are the values comes with the paremeters.
        self.lastName = lastName
        self.age = age

person1 = Person("Muhammet", "Banzaroğlu", 33)
print(person1.firstName)
print(person1.lastName)
print(person1.age)
#%%
#Class for employee for ex.
#INHERITANCE STRUCTURE
Class Worker(Person) : # We attached the common class to more detailed other classes. Both 'Worker' class and 'Customer' class includes 'Person' class
    def __init__(self, salary):
        self.salary = salary
Class Customer(Person) :
    def __init__(self, cardNumber):
        self.cardNumber = cardNumber

ahmet = Worker()
ahmet.firstName
ahmet.lastName
ahmet.age
ahmet.salary # ahmet can reach all of these subject from class of Worker and Person



