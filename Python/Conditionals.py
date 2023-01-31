#Important topic in programming. Helps to build algorithms. 
#In python the block structure will be displayed with indentations. There is no bracelet for "IF" or "FOR" functions.
#Leave a 'tab' inside of each block structure.
#%%
num1 = 10
num2 = 20

#a basic condition

if num1 > num2 :
    print("Number1 is bigger than number 2")
    print("Number1 is bigger than number 2")
    print("Number1 is bigger than number 2")
    print("Number1 is bigger than number 2")
    print("Number1 is bigger than number 2")
    print("Number1 is bigger than number 2")
    #these lines in a block structure. they all will be displayed for if number1 is bigger than number 2 condition.
elif num2 > num1:
    print("Number2 is bigger than number1")
else :
    print("Given numbers are equal.")
    
#%% 
#Trying the solve an example in an efficient way. Finding the biggest input of all the given uncertain number of inputs.

myList = [] #declared a list of integers.

while True :
    user_input = str(input("please enter a number. Press SPACE to stop \n"))
    
    if len(user_input) == 0:
        break
    try:
        myList.append(int(user_input)) # The try block lets you test a block of code for errors.
        #the code will try to execute the operation inside of the try block. If it encounters with a error,
        #then it will execute the except block
    except ValueError : # The except block lets you handle the error.
        print("Invalid Value")
        continue 
print(myList)
biggestValue = myList[0]

for i in myList :
     if i > biggestValue :
        biggestValue = i 
     else :
        continue
print("Biggest value of given inputs is : " + str(biggestValue))
 #%%   