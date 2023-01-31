#Dividind a semtence into its words 

sentence = "And tonight , lets enjoy life"

words = sentence.split() #splits each word in the given string
print(sentence)
print(words)
words.sort() #put the words in order alphabetically
print(words)

for word in words:
    print(word)