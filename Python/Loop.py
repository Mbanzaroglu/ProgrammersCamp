%%
#FOR LOOP-------------------------------------
cities = ["istanbul", "İzmir","Ankara","Trabzon"] # a basic list of cities

for city in cities : # "city" is a keyword. it is not important what it is called. It is a temp nickname.
    print(city) #it prints all the elements of "cities" in order. 
    print(city[0:2]) #it will print out the first 2 char of strings in the list (an, iz, is)
    # lets use if condition inside of for
    if city == "Ankara" : 
        #there is another indentation for if blockk
        print("Capital") # prints it for only Ankara
        break #it ends the loop that exist above. If there is more than one for within, it will end the inner one..
    print("Not Capital") #prints for cities except Ankara. 
    
    print(city) #it prints all the elements of "cities" in order. 
    print(city[0:2]) #it will print out the first 2 char of strings in the list (an, iz, is)
    # lets use if condition inside of for
    if city == "Ankara" : 
        #there is another indentation for if blockk
        print("Capital") # prints it for only Ankara
        continue #it interrupts the loop that exist above when this condition occured but continues to the loop keeps iterating. 
    print("Not Capital") #prints for cities except Ankara. 
#%% 
#WHILE LOOP--------------------------------------
#it keeps running until a specific condition is satisfied. 

#lets count from 1 to 10.

counter = 1
_sum = 0
while counter <= 10 : 
    _sum =counter +_sum 
    #For loops can iterate by itself but you need to dictate the iteration in while loop. 
    counter = counter + 1 # For looop can increase the counter by itsef in every iteration. But while loop cant.
print(_sum)
#%%

#RANGE FUNCTİON FOR LOOP -----------------------------------

for x in range(100) : 
    print(x+1) #it prints the numbers from 0 to 99, 100 items will be printed but 100 hasn't been printed.
    # if we write x+1, then it starts from 1 and end with 100.
for x in range(1,10):
    print(x) #prints from 1 to 10 but 10.
for x in range(1,100,2): #these 3 integers is called start point, end point and step, respectfully.
    print(x) #prints numbers startin from 1 to 100 -not including 100- by increasing 2 each time.
    
#%%