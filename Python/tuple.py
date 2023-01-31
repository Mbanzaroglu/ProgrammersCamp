#we will cover the tuples, they are like lists but the items are not changeble after declaration.
#tuples are READ ONLY while lists are READ/WRITE
#%%
listDeclaration = [] #items inside 
tupleDeclaration = () # only difference in declaration is the type of bracelet.

tupleExample = (2,4,6,"Ankara",(1,3,5), [" "]) # can be put a tuple in list and list in tuple.
listExample = [2,4,6,"Ankara",[1,3,5],(" ")] # elements doesnot need to be same, just to show the difference between tuple and list.

print(type(tupleExample))
print(type(listExample))
# <class 'tuple'>
# <class 'list'> will be returned.
print(tupleExample)
print(listExample)
#prints the items inside.

listExample[0] = 5 # this works flawlessly 
#tupleExample[0] = 5 # TypeError: 'tuple' object does not support item assignment

print(tupleExample[-2])
print(listExample[-2])
# calls the second to last items each.
#%%
#----------------------------------------------------
#if the tuple has one elements, there need to be a comma in the end for ex:
    
value = ("Banz")
value2 = ("Banz",)
print(type(value))
print(type(value2))
# <class 'str'>
# <class 'tuple'> will be returned.
#also when you print one item from the tuple it will put comma in the end in order to prevent confusion with LIST

print(tupleExample[0:1])   # (2,) 
print(listExample[0:1])    # [5]    these values will be returned.
#%%