# Example 1

# we ask the user to input their age, then save it in a variable user_age

user_age = input("please enter your age: ")
user_age = int(user_age)
if user_age >= 50: # we will experience a runtimr error here because the input given will be an int
                   # but we havent concatinate it into an int by first returning and saving the user_age into an
                   # int or by creating another variable. (user_age = int(age).
    #print("you are user_age years old") # this is a runtime error because the program will run with out an error but 
    # the desired result is not what is expected or gotten.

    print(f"you are {user_age} years old")


# Example 2.
'''
my_hobbies = ["Dancing", "Singing", "Playing video Games", "Eating"]
print(my_hobbies[4])

# we will have a run time error because in python numbering starts from 0
# and i have requested for a number that is not on my list.
'''


