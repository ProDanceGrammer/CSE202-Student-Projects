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

# Function to combine two function which it accepts as argument
def compose_function(f, g):
     return lambda x : f(g(x))

# Function to add 3
def add_3(x):
    return x + 3

# Function to mutiply 5
def mul_5(x):
    return x * 5

# Function to subtract 1
def sub_1(x):
    return x - 1

# Composite function returns a lambda function. Here add_sub_mul will store lambda x : mul(sub(add(x)))
add_sub_mul = compose_function(compose_function(mul_5, sub_1), add_3)

# Asking a number
try:
    # Asking to write a number
    number = int(input('Please enter a number: '))
except:
    # Returning an error message if there would be not a number
    print("There is not a number. Please restart a program to write a number again")

# Printing a result
print("Adding 3 to ", number, ", then subtracting 1 and multiplying the result with 5: ",
          add_sub_mul(number))



# Saying

#Function to make little letters
def whisper(text):
    return text.lower()

#Function to make capital letters
def shout(text):
    return text.upper()

def say(say_type, text):
    return say_type(text)

# Asking for a type of saying
try:
    # Asking to write a number
    type_of_saying = int(input('Please enter a number 1 if you want me to whisper to you, or write me 2 to shout on you: '))
except:
    # Returning an error message if there would be not a number
    print("There is not a number. Please restart a program to write a number again")

if type_of_saying != 1 and type_of_saying != 2:
    # Returning an error message if there would be not a correct number
    print("There is not a number of 1 or 2. Please restart a program to write a number again")
else:
    # Asking to write a text
    text = str(input('Please enter a text to say to you: '))

    if type_of_saying == 1:
        # Whispering user's text
        print(say(whisper, text))
    else:
        # Shouting user's text
        print(say(shout, text))
