#we will work on the data in the users.json file.

import json 

with open("users.json") as jsonData : 
    data = json.load(jsonData)
print(data) #prints all data 
print(data[0]) #prints first user
print(data[0]["username"]) #prints first user's user name
print(data[0]["address"]["geo"]["lat"]) #it reaches the lat information inside of the geo inside of the adress
     #which is finally inside of the first user's index.
     
#for example I want all of the users names and adresses and e-mails only. Not other info.

for x in range(10) :
    print(data[x]["name"])
    print(data[x]["address"])
    print(data[x]["email"])

       
        