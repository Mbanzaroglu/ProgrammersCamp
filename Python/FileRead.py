#%%
#As a developer, we will mainly pull data from another sources and execute them in a manner.
#first of all we need this external file. 

# f = open("customer.txt") # it calls the txt file called customer.txt. 
# #but there is no such file 
# f = open("customer.txt","w") # it writes over the file presented. If the file doesn't exist it creates one. 
# f = open("customer.txt","a") # Read/write. Visualizing the file and Adding a new value file. ('a comes from append')
# f = open("customer.txt","r") # Cant change the file, just to read.
# f = open("customer.txt","x") # Create a file. If it already exist, then gives an error.

f = open("customers.txt") #default form of open() function is to read.
#first method for read
print(f.read()) #it prints all the values in 'customers.txt' respectfuly
print("***********")
#second method for read
print(f.readline())
print(f.readline())
print(f.readline()) #'readline()' functions read the file line by line. It leaves o blank line in between. 
                    #Reads the unread lines. If the line 12 was active, the lines 15,16,17 wouldn't work
#third method for read
for l in f :
    print(l) # it prints all the lines that is unread.
    

f.close() #close the file when the file is finished.
#%%

fileToAppend = open("students.txt","a")

fileToAppend.write("Tarık Aşçı") #writes it in file
fileToAppend.write("\n") #new line
fileToAppend.write("Kerem Guler") #new data to write
#writing in the 'append' format allows you the write the data next to previous data. Writing in the 'writing' format overwrites the data 
#and deletes the existing ones. So BE CAREFUL!!
fileToWrite = open("students.txt","w")
fileToWrite.write("Muhammet Banzaroğlu") #now there is only 'Muhammet Banzaroğlu' exist in the file.
fileToAppend.close() #write these 2 lines first and then fill between.
#%%
#If you want to delete the students.txt file then:
    
import os 
if os.path.exist("students.txt") :# check if it exists 
    os.remove("students.txt")
else :
    print("file couldn't found.")