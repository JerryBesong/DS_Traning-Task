# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

animal = "Lion"   # NameError. variable Lion not known because its not on colons "" as a string
animal_type = "cub"
number_of_teeth = 16

full_spec = f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth" # This wasnt called with a function (f)
# also the placeholders wasnt placed right with its values.

print(full_spec) # SyntaxError: Missing parentheses() in call to 'print'

word = "My Name is Jerry Besong"
wordword = range(len(word.split()))

word2 = len(word)
word2 = (word)[-1:-13:-1]
for i in wordword:
    print(wordword[4])
    

print(word2.upper())