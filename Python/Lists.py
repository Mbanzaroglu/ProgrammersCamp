#%%
mylist = [] #an empty list
mylist = [1,2,3,4,5] #list of integers
mylist = [1,2,3.0,"Hello World!"] #list of mixed types of variables.

studentsList = ["Muhammet","Banzaroğlu","Oğuz","Deren"]

print(studentsList[1])#list first index
print(studentsList)#list all of them

studentsList.append("Samet") #added student named Samet
print(studentsList)
studentsList.remove("Deren") # Deren removed from the list
print(studentsList)
#%%
#applying functions in the lists.------------------------------

#print(studentsList.clear())#clear the list
print(studentsList)#prints an empty list

#Finding the amount of repetitive items-----------------
studentsList.append("Muhammet") # added another Muhammet to the list
print(studentsList.count("Muhammet"))
print(studentsList)
print("The number of Muhammet in the list is : " + str(studentsList.count("Muhammet")))
#printing the number of total Muhammets in the list above
#---------------------------------------------------
#finding the index of item ------------------------------------
print("The number of index of Muhammet is = " + str(studentsList.index("Muhammet")))
#---------------------------------------------------
#deleting an item with its index not the name of it
print(studentsList.pop(1)) #printed the item will be removed.
print(studentsList)#printed after removal.
#---------------------------------------------------
#inserting an item in the specified index of the list 
studentsList.insert(1, "Banzaroğlu")
print(studentsList)
#---------------------------------------------------
#inverting the items indexes
studentsList.reverse() # inverted the items
print(studentsList)
#---------------------------------------------------
#backup the list items
backupList = studentsList #they are both the same thing, it is not a copy
backupList[0] = "Ahmet"
print(str(studentsList) + "\n" + str(backupList)) 
#we changed the backupList but the studentsList is changed also!!!

backupList = studentsList.copy() #Now this is a copy of others. Now we can change freely.
backupList[0] = "Ahmet"
print(str(studentsList) + "\n" + str(backupList)) 
#---------------------------------------------------
#%%
#extending a list 
extension = ["Funda", "Pınar"]
studentsList.extend(extension) # to add a list of elements
print(studentsList) #we added the items of list(extension) to out studentList
studentsList.append("Toros") # to add single item
print(studentsList)
#%%
#---------------------------------------------------
#listing the elements alphabetically or numerically 
studentsList.sort() #we put them in order
studentsList.reverse() #after sort operation, we inverted it and obtained the reverse order.
#%%


