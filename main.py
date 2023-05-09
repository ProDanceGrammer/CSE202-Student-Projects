

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



# Composing



# Sorting




