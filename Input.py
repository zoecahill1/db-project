# Zoe Cahill - Applied Databases Project
# File containing menu text and input validation

# Function which displays menu text
def display_menu():
    print("")
    print("World DB")
    print("-" * 7)
    print("MENU")
    print("=" * 7)
    print("1 - View 15 Cities")
    print("2 - View Cities by population")
    print("3 - Add new city")
    print("4 - Find car by engine size")
    print("5 - Add new car")
    print("6 - View countries by name")
    print("7 - View countries by population")
    print("x - Exit application")

# Input validation to make sure input is positive number
def getNum(x):
    while True:
        try:
            # Tries to cast input as int, if it fails will give a ValueError
            num = int(input(x))
            # Code to catch negative numbers
            if num < 0:
                print("Please enter positive numbers only")
                # Will loop until positive number entered
                continue
            break

        # Catches above ValueError if it occurs
        except ValueError:
            print("Please enter integers only")
            continue
    # Number is returned once all above checks are passed
    return num

# Input validation to make sure only <, > or = are entered
def getSymbol(x):
    while True:
        # Assigning input
        symbol = input(x)
        try:
            # Checking symbols
            if ((symbol == "<") or (symbol == ">") or (symbol == "=")):
                # If they match symbol is ok to be returned to main function
                break
            else:
                # Anything else will keep looping until symbol matches
                print("Please only enter <, > or = only")    
                continue
        # Will catch any other errors which occur
        except:
            print("An error has occured")
    # Returns symbol to main program
    return symbol 

# Input validation to check for float
def getFloat(x):
    while True:
        try:
            # Tries to cast variable to float will give ValueError if fails
            num = float(input(x))
            # Checking for negative values
            if num <= 0:
                print("Please enter positive numbers only")
                continue 

        # Catches value error if occurs
        except ValueError:
            print("Please enter a decimal number")
            continue
        # returns variable if it passes checks
        return num

# Input validation to check for A-Z characters only
def getLetters(x):
    while True:
        string = input(x)
        # isalpha checks if A-Z character
        if string.isalpha():
            # if it matches returns string to main function
            return string
        # If not will print this message
        print("Please enter characters A-Z only")

