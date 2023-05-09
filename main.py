

# Mapping

# Function "twice" will return a number multiplied by two
def twice(i):
   return i*2


# Asking for a list of numbers
try:
    numbers = [int(x) for x in input('Please enter a list of numbers, which are separated by spaces: ').split(" ")]
# Returning an error message if there would be not a list of integers
except:
    print("There are not only numbers in your list. Please restart a program to write elements in list again")

# Mapping a list
twiced_numbers = list(map(twice, numbers))
# Printing a result
print("Your list of numbers multiplied by 2: ", twiced_numbers)

# Filter



# Reducing



# Composing



# Sorting




