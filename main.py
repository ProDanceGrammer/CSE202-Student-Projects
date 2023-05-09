from functools import reduce

# Mapping

# Function "twice" will return a number multiplied by two
def twice(i):
   return i*2

def ask_numbers_list():
    try:
        # Asking to write numbers
        numbers = [int(x) for x in input('Please enter a list of numbers, which are separated by spaces: ').split(" ")]
        return numbers
    except:
        # Returning an error message if there would be not a list of integers

        print("There are not only numbers in your list. Please restart a program to write elements in list again")

# Asking for a list of numbers
numbers_to_map = ask_numbers_list()

# Mapping a list
twiced_numbers = list(map(twice, numbers_to_map))
# Printing a result
print("Your list of numbers multiplied by 2: ", twiced_numbers)



# Filter

# A function that will return true, if in the variable is one of planets og solar system
def IsInSolarSystem(planet):
    solar_system = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    if planet in solar_system:
        return True
    else:
        return False

# Asking for a list of planets
planets = [str(x) for x in input('Please enter a list of planets, which you would like to filter out: ').split(" ")]

# Filtering a list out
filtered_list = list(filter(IsInSolarSystem, planets))

# Printing a result
print("Here is a list of planets, which are placed in solar system: ", filtered_list)




# Reducing

# A function that returns a sum of elements
def add(a, b):
    sum = a + b
    return sum

# Asking for a list of numbers
numbers_to_reduce = ask_numbers_list()

# Reducing a list by add function
reduced = reduce(add, numbers_to_reduce)

# Printing a result
print("Here is a sum of your elements: ", reduced)







# Composing






# Sorting




