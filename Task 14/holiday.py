# This is program that calculates the total holiday cost of a customer.
# These total cost includes PLANE COST, HOTEL COST and CAR-RENTAL COST.

print("Hello, Welcome To Prudence Travel Agency Ltd.\n")    

# collected data from the user using input

city_flight = input("Please enter your desired destination.\nHere are options of our travel destinations (Italy, Nigeria, South Africa, United Kingdom, Canada': ").lower().rstrip().strip()

num_nights = int(input("Please enter the numbers of night you will be staying in the hotel : "))

rental_days = int(input("Please enter the numbers of days you will be renting a car : "))

# created three functions to make the program calculation easy when ever we will be needing to calculate.

def hotel_cost(num_nights):
    return (num_nights * 300)
    
def plane_cost(city_flight):
    return flight_cost

def car_rental(rental_days):
    return rental_days * 70

def holiday_cost(hotel_cost, plane_cost, car_rental):
    return (hotel_cost(num_nights) + plane_cost(city_flight) + car_rental(rental_days))

# using a loop statement to give verity of flight destination and cost to our user

while True:
    if city_flight == "italy":
        flight_cost = 750 
        break
    
    elif city_flight == "nigeria":
        flight_cost = 1000
        break
    
    elif city_flight == "south africa":
        flight_cost = 970
        break
    
    elif city_flight == "united kingdom":
        flight_cost = 1390
        break
    
    elif city_flight == "canada":
        flight_cost = 1500
        break
    
    else:    
        print("Unfortunately there was an error please confirm destination again")
        city_flight = input("Please enter your desired destination.\nHere are options of our travel destinations (Italy, Nigeria, South Africa, United Kingdom, Canada': ").lower().rstrip().strip()

# print all calculated steps with the help of my function
 
print(f"The hotel cost is {hotel_cost(num_nights)}")
print(f"The plane cost for {city_flight} is {plane_cost(city_flight)}pp")
print(f"Car rentals for {rental_days} is {car_rental(rental_days)}")
print(f"Total Holiday for {city_flight} is = {holiday_cost(hotel_cost, plane_cost,car_rental)} pp")
print("Thanks for petronising us")

