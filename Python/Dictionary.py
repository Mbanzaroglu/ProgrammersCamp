#DICTIONARY holds the data out of order. 
#it is like a regular dictionaries in real life. Different data types can be hold in it.

my_Dictionary = {1 : 'apple',  2 : 'ball'}  #mixed keys "1" and ""2" are considered as keys and the value after colon is data
        

Dict = {"key":"value", "book" : "Sefiller", "Movie" : "Shutter Island"}  

#reaching a certain value in given index. Index here is "key" parameter since there is no order in dictionaries.

print(Dict["book"]) # prints out "Sefiller"

#Changing a value of key

Dict["book"] = "Beyaz Diş" # changes the value for "book".
          
#There is a different way to declare a dictionary

Dict_2 = dict(book = "Vadideki Zambak", movie ="Can Dostum")    

print(Dict)
print(Dict_2)  
#output will be like below
# {'key': 'value', 'book': 'Beyaz Diş', 'Movie': 'Shutter Island'}
# {'book': 'Vadideki Zambak', 'movie': 'Can Dostum'}