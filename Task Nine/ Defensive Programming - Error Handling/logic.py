# Our job is to write a program in Python that will help to separate Even and Odd Numbers from a list of numbers.
# and then store them in two different list.

# We can either generate these numbers ourselves or get them from a list of data with even and odd numbers in them.

# IN THIS PROGRAM WE WILL MAKE USE OF: FOR LOOP, (LIST(RANGE), MODULE (%) AND APPEND FUNCTION.

# now we will first create the list with these numbers.

list_of_numbers = list(range(1,100))
#list_of_numbers = (input("please enter a maximum number \nas we want to seperate the even numbers from the \nodd numbers\n: ")))
# create an empty varaiable where even numbers and odd numbers will be saved.

even_numbers = []
odd_numbers = []

# Now lets iterate our list of numbers (one by one) to check the numbers if they can be divided by 2.
# when iterating, if a number is divided by 2 then we will store it in the even variable
# but if not, we will store it the odd varaiable

for numbers in list_of_numbers:
    if numbers / 2 == 0:    # this command is supposed to be in module (% 2) instead i changed it to / 2.
        even_numbers.append(numbers) # and then save the number in even number if devided without remaining.
            
# else the the below statement will be activated if there is a remain when divided by 2 and then stored as an odd number.
        
    else:
        odd_numbers.append(numbers)
print("")
print(f"These are the 'Even' numbers {even_numbers}",)
print(f"These are the 'Odd' numbers {odd_numbers}")


# this gave me an answer but not what i was expecting to get.

print("Thank You")