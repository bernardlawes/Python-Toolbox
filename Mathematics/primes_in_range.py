# Create a range of prime numbers between 1 to n
# key thing is the filter function, The Filter function returns an iterator yielding those items of 
# iterable for which function(item) is true. If function is None, return the items that are true.
# This a a more efficient approach to the more naïve or "alternative" options like nested loops or 
# list comprehensions with repeated work


# Create a range of numbers from 1 to 999
nums = range(1, 100)

# Convert the range to a list
listOfNumbers = list(nums)

# Define a function to check if a number is prime
def is_prime(num):
    # Check divisibility from 2 to num-1
    for x in range(2, num):
        if (num % x) == 0:
            return False
    return True

# Filter the list of numbers to get only prime numbers
primes = filter(is_prime, nums)

# Convert the filtered iterable of prime numbers to a list
listOfPrimes = list(primes)

# Print the list of prime numbers
print(listOfPrimes)