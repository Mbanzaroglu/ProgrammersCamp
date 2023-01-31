
#%% Printing all of the customers First and Last Name
import sqlite3 #we are importing this module in order to work with the sqlLites based DataBase

connection = sqlite3.connect("chinook.db") # this .db file is already existed file which is in our directory.
#if you write database name incorrect, it creates a new one. 

cursor = connection.execute("select * from customers")# '*' means all the columns in customers.

for column in cursor :
    print("First Name =" + column[1])
    print("Last Name =" + column[2])
    print("*************")
#%% Printing specified customers First and Last Name and Countries.
cursor2 = connection.execute("""select FirstName,LastName,Country 
                             from customers 
                             where city ='Prague' or city = 'Berlin' 
                             order by FirstName""") #since the command line can be too long, use 3 quotes to use multiple lines. More readable
# 'order by' function can order FirstName alphabetically. 'order by FirstName desc' can reverse it.

#it prints the customers first and last name from prague or Berlin
for column in cursor2 :
    print("First Name =" + column[0])#index is zero because we now have 2 column and FirstName is the index 'zero'
                                    #in cursor, we had all columns therefore the FirstName was the index 'one'
    print("Last Name =" + column[1])
    print("Country = " + column[2])
    print("*************")
#%% 'group by' and 'having' modules

cursor3 = connection.execute("""select city, 
                             count(*) from Customers 
                             group by city having count(*)>1 order by count(*) desc""") #selects all the columns and counts the number of the same cities.
                             #listing them according to count in descending order.
for column in cursor3 
    print("City =" + column[0])
    print("Count =" + str(column[1]))
    print("*************")  
                           
#%% 'like' function.
cursor4 = connection.execute("""select FirstName,LastName
                             from customers
                             where city like '%a%' """)# it fetches the names and last names
                             #from the cities that letter a within .
# '%' at the left means that the previous part doesn't matter. At the right, means the after doesn't matter.
# a% means start with 'a' or %a means ends with'a'.
for column in cursor4 :
    print("First Name =" + column[0])
    print("Last Name =" + column[1])
    print("*************")
#%% INSERTING A NEW VALUE TO DATA BASE
def insertCustomer():
    connection = sqlite3.connect("chinook.db")
    connection.execute("""insert into customers (firstName, lastName, city, email) 
                       values ("Muhammet","Banzaroglu","Trabzon","banzaroglu20@itu.edu.tr")""")

    connection.commit() #commiting the changes to database
    connection.close()

insertCustomer() #We can also send parameters when we call the function 
#%% UPDATING THE CURRENT DATA

def updateCustomer():
    connection = sqlite3.connect("chinook.db")
    connection.execute("""update customers 
                       set city = 'Istanbul' 
                       where city = 'Trabzon' """)   
    connection.commit()
    connection.close()

updateCustomer()

#%% DELETING A DATA FROM DATABASE

def deleteCustomer():
    connection = sqlite3.connect("chinook.db")
    connection.execute("""delete from customers 
                       where customerid = 61 """)   
    connection.commit()
    connection.close()

deleteCustomer()












    