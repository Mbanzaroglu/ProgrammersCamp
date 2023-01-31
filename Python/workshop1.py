
#switching the values of variables with each other

x = 10 
y = 20

print("x = " + str(x))
print("y = " + str(y))

print("When we exchange the values : \n")

temp = x # assing temp. value to hold the value of X while we assigning the value of y to x.

x = y
y = temp 

print("x = " + str(x))
print("y = " + str(y))

#there is a feature specific to python which allows us to : 
    
x,y = y,x 
print("When we exchange the values back : \n")
print("x = " + str(x))
print("y = " + str(y))