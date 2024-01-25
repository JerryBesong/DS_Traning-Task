# first was to create our list of menu
# alos created stock and price dictionary
menu = [
    "Cold Brew", 
    "Espresso", 
    "Lattes", 
    "Cappuccino", 
    "Cortado", 
    "Drip Coffee"
    ]

# want to check if certain input or word can be found in our list.
# using an if statement
# ask for an input

'''
word = input("please give us a word: ")
if "Cold Brew" in menu:
    print("Yes, Element found in menu")
else:
    print("No, Element not found in list")
    
# For traning purpose, i created another extended list so we can use the
# extend function (.extend())
'''

'''
ex_menu = [7, 8, 9, 10, False, "Jerry"]
menu.extend(ex_menu)
print(menu) # this way prints an extention of the menu by addint the ex_menu
print(menu.extend(ex_menu)) # or we just add the function directly yo our print function

# using the popped fucntion to pop an element from the list
# popped_name = menu.pop()
# print(popped_name)
'''

# using the insert function to add to our list in menu
# also assigning an argument of where the inserted element should be

'''
popped_name = "Nigerian Coffee"
menu.insert(2, popped_name)
print(menu)
'''


stock = {"Cold Brew": 10, 
         "Espresso": 20, 
         "Lattes": 30, 
         "Cappuccino": 40,
         "Cortado": 50,
         "Drip Coffee": 60}
'''
# how to pop in dictionary

popped = stock.pop("Cold Brew")
print(popped)
'''

'''
# another way to pop an element in a dictionary
print(stock["Cortado"])
'''

price = {"Cold Brew": 5.00, 
         "Espresso": 23.00, 
         "Lattes": 8.90, 
         "Cappuccino": 10.15,
         "Cortado": 2.10,
         "Drip Coffee": 6.00}

'''
# how to print elements in price dict
for i, j in price.items():
    print(f"{i} : {j}")
'''

'''    
# how to print just values from a dict

for i in price.values():
    print(i)

# How to print just the keys in dictionary

for i in price.keys():
    print(i)
'''
'''
# how to add an element to dictionary
price["Jerry Besong"] = 31
print(price)
'''
'''
# How to update an element in a dictionary
price["Cold Brew"] = 100
print(price)
'''
'''
# How to reference value element in dict
reference = price["Cappuccino"]
print(reference)
'''
'''
# HOW TO USE THE GET FUNCTION IN DICT
# NOTE THIS FUNCTION WORKS ONLY WHEN YOU NEED TO GET A VALUE USING KEY
getfunction = price.get("Lattes")
print(getfunction)
'''


# created a vraiable where our total stock will be returned

total_stock = 0

# using the loop function to iterate through our menu list
# print total stock for our answer
for items in menu:
    item_value = (stock[items] * price[items])
    total_stock += item_value
    
print(f"The Total Stock is {total_stock}")

'''
__name__ = ["Jerry Besong", "Prudence Osa-asemota", "Joe Brown"]

for i in __name__:
    print(i)

for i in range(len(__name__)):

    print(__name__[i])
    
'''