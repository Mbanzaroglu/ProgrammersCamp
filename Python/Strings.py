 
message = "Hello World!"
#we will try to pick the different parts of the string.
print(message[2])
 # every string is an array and each variable is an element of array.
print(message[2:5])
 # it gives us every index from two to five but five and including two.
print(message[2:])
 # it gives us every index from two to end of the string.
#--------------------------------------------------------------- 
cut_message = print(message[2:5])
 # it assigns the 3 index from two to five to another variable
 #---------------------------------------------------------------
print(len(message))
# if the given word comes from third party file and the number of index is needed.
#---------------------------------------------------------------
print(message[len(message)-1:len(message)])
#it gives us the last element of string
#--------------------------------------------------------------- 
print(message.upper()) #turns all elements to uppercase 
print(message.lower()) #turns all elements to lowercase
#lower and upper function for the given strings.
#Since the upper and lower case are different things in programming, when the 2
#different strings needed to be compared but although the text are the same,
#there is difference in the capitals. It is useful for comparison.
#---------------------------------------------------------------
print(message.replace("H","h"))#replaces all 'H' with 'h'
print(message)
#it is used to replace any element in the given string
#---------------------------------------------------------------
sentence = "Muhammet Banzaroğlu Computer Engineering"
print(sentence.split())#if it is not defined, it breaks it when encountered with the blanck space
# if the given string is sentence, it subtracts the defined pieces.
#default is blank space  
print(sentence.split()[2])
#split it according the rule and pick the second index and write it out.


#INPUTS-------------------------------------------------------------

name = input("Please write your name : ")
#it prints out the given statement and requires an input and assigns it to defined variable.




      