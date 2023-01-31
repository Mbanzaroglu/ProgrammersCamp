# SET has no index and no order in items. It is declared by curly braces.
# there is no repetitive items inside. All items are unique. 
# Items are not changeable. But an item can be added or substracted.
#%%
a_set = {}

studentSet = {"Muhammet", "Banzaroğlu", "Engin", "Mete"}
print(studentSet)
# {'Engin', 'Banzaroğlu', 'Muhammet', 'Mete'} prints in this order, according to itself. there is no rule for that

for student in studentSet:
    print(student)
#prints in the same order before. The order doesnot change each time it is printed.

print("Derin" in studentSet) #it is a boolean operation, it returns true or false according to existence of given name.
#return FALSE
#OR

if "Derin" in studentSet:
        print("Derin ismi listede var")
else:
        print("Derin ismi listede yok")
        
#If you want to add an element:------------------
studentSet.add("Ali")
print(studentSet)
#"Ali" has been added successfully 
#%%
#if you want to add multiple elements :

newSet = {"Selin","Gizem"}
newList = ["Okan","Umut"]
    
studentSet.update(newSet) #you can add it a  set
print(studentSet)
studentSet.update(newList) #you can add it a list
print(studentSet)
studentSet.update(["Tarık","Deniz"]) # you can add items manually without set, list or tuple 
print(studentSet)
#%%
#if you want to remove an item ---------------------------
studentSet.remove("Selin") #you can remove an item
print(studentSet)
#studentSet.remove(newSet)#but you cant remove a set or list that has been added earlier.
print(studentSet) # It will cause an ERROR

#if you want to remove an item but the item is already doesn't exist, remove() function will
#cause an error. If you want to avoid ERROR : 
    
studentSet.discard("İlkkan") # there was no operation executed but still no error occured.
print(studentSet)
#%%
#Cleaning all items from SET.-------------------------

studentSet.clear()
print(studentSet) # the output is "set()". It is empty.
# the SET still exist but empty.

del studentSet
print(studentSet) # it doesnt exist no more. This print function in line 59 will cause an error.

# #SET UNION--------------------------------
# #For example you have 2 lists and these two lists has items in common. 
# #Set Union is a method which unites these two sets but doesn't writes the common elements twice.

W
setA = {1,2,3,4,5}
setB = {1,3,4,6,7,8}

print(setA | setB )
#or
print(setA.union(setB))#there is defined function for this.
print(setB.union(setA)) #line 71 and 72 are the same thing.
#Now, set A and set B are still same. We can assign union set to a new set.

x = setA | setB
print(x) # Now the X is the union of setA and setB

#%%
# SET INTERSECTION --------------------------------------


setA = {1,2,3,4,5}
setB = {1,3,4,6,7,8}

print(setA & setB )
#or
print(setA.instersection(setB))#there is defined function for this.
print(setB.instersection(setA)) #line 87 and 88 are the same thing.
#Now, set A and set B are still same. We can assign intersection set to a new set.

x = setA & setB
print(x) # Now the X is the intersection of setA and setB

#%%
# SET DIFFERENCE --------------------------------------


setA = {1,2,3,4,5}
setB = {1,3,4,6,7,8}

print(setA - setB )
#or
print(setA.difference(setB))#there is defined function for this.
print(setB.difference(setA)) #line 103 and 104 are the same thing.
#Now, set A and set B are still same. We can assign difference set to a new set.

x = setA - setB
print(x) # Now the X is the difference of setA and setB

#%%


