# Zoe Cahill - Applied Databases Project
# Main
import SQL
import Input
import Mongo
import pymysql
import pymongo

# Main method which calls various functions in menu
def main():

    # Function displays the main menu text
    Input.display_menu()

    # Will keep looping so menu stays active until x is entered later and loop is broken
    while True:
        choice = input("Enter choice: ")

        # Menu 1: View first 15 cities in world database
        if (choice == "1"):
            # Calls function which contains sql query
            SQL.viewCities()
            # Reverts to menu text once finished
            Input.display_menu()

        # Menu 2: Cities by Population
        elif (choice == "2" ):
            # Calls input validation to make sure only symbols <, > or = are entered
            s = Input.getSymbol("Please enter <, > or =: ")
            # Calls input validation to make sure only positive numbers are entered
            n = Input.getNum("Please enter a number: ")
            # Calls function with SQL query
            SQL.viewCitiesPop(s,n)
            # Reverts to menu text once finished
            Input.display_menu()

        # Menu 3: Add new city
        elif (choice == "3"):
            while True:

                name = input("Enter city name: ")
                # Calls input validation to make sure only characters A-Z are entered
                code = Input.getLetters("Enter country code: ")
                dist = input("Enter district: ")
                # Calls input validation to check if positive integer only
                pop = Input.getNum("Enter Population: ")
                # Will try function to addCity SQL query
                try:
                    SQL.addCity(name,code,dist,pop)
                # IntegrityError will occur if country code does not match current database
                # will keep looping until error no longer occurs
                except pymysql.err.IntegrityError as e:
                    print("**ERROR** Country code" ,code, "does not exist" )
                    continue
                break
            # Will print when addCity is successful
            print("Record Added")
            # Reverts to menu text when finished
            Input.display_menu()

        # Menu 4: Find car by engine size
        elif (choice == "4"):
            # Calls function with mongo query
            Mongo.findCarEngine()
            # Reverts to menu text when finished
            Input.display_menu()

        # Menu 5: Add new car
        elif (choice == "5"):

            while True:
                try:
                    # calls function with mongodb query
                    Mongo.addCar()
                # catches error if carID already exists as it is a key
                except pymongo.errors.DuplicateKeyError:
                    print("This car ID already exists try again")
                    # will continue to loop until error does not occur
                    continue
                break

            # reverts to menu text once finished
            Input.display_menu()

        # Menu 6: View countries by name
        elif (choice == "6"):
            # calls input validation check for character a-z only
            string = Input.getLetters("Please enter name or part of name: ")
            # calls function with sql query
            SQL.countryName(string)
            # reverts to menu text once finished
            Input.display_menu()

        # Menu 7: View country by pop
        elif (choice == "7"):
            # calls input validation to check <, > or = entered only
            s = Input.getSymbol("Please enter <, > or =: ")
            # calls input validation to check for positive interger only
            n = Input.getNum("Enter a number: ")
            # calls function with sql query
            SQL.countryPop(s, n)
            # reverts to menu text when finished
            Input.display_menu()

        # Menu x: Will exit program by breaking from loop
        elif (choice == "x"):
            print("Goodbye!")
            break

        # Any other character will just display menu
        else:
            Input.display_menu()


if __name__ == "__main__":
    main()