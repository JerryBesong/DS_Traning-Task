# in this task we are expected to create a pattern as shown below
# first we need to know how many rolls and colum will be needed to solve this problem
# Now we know, next is to create the varaiables

num = 9
pattern = "*"

# we are told to use a single (for loop)

for i in range(1, num + 1):
    complete_shape = pattern * i
    #print(complete_shape) 

# Because we already understood the coloum where we need to do the reverse from the pattern given.
# created variables to hold the reverse of the pattern
    if i >= 5:
        countdown = (num + 1 - i)
        complete_shape = pattern * countdown
    print(complete_shape)
