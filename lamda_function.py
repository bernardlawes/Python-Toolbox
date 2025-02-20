# Lambda functions are small anonymous functions that can have any number of arguments, but can only have one expression.
# Lambda functions can be used to replace simple functions that are only used once in a program.

# List of cars with details (brand, model, year, price, mileage)
cars = [
    ("Toyota", "Corolla", 2019, 15000, 10000), 
    ("Toyota", "Camry", 2019, 25000, 20000), 
    ("Ford", "Fiesta", 2019, 14000, 5000), 
    ("Ford", "Focus", 2019, 16000, 10000), 
    ("Honda", "Civic", 2018, 18000, 15000), 
    ("Honda", "Accord", 2018, 22000, 25000)
]

# Define a function to calculate cost per mile for a car
def cost_per_mile(s):
    return s[3] / s[4]  # price / mileage

# Sort the list of cars based on cost per mile using the defined function
sorted_cars = sorted(cars, key=cost_per_mile)
print(sorted_cars)  # Print the sorted list of cars


# Sort the list of cars based on cost per mile using a lambda function
sorted_cars = sorted(cars, key=lambda s: s[3] / s[4])
print(sorted_cars)  # Print the sorted list of cars