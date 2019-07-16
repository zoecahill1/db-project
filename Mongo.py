# Zoe Cahill - Applied Databases Project
# File containing all functions relating to monogoDB queries
import pymongo
import Input

# Setting up mongo connection
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mongo"]
mycol = mydb["mongo"]

# Menu 4: Find car by engine size
def findCarEngine():
    # Calls input validation to check for float
    size = Input.getFloat("Please enter engine size: ")
    # mongoDB query
    query = {"car.engineSize":size}
    x = mycol.find(query)

    # counts rows in resutls if over zero prints results
    if x.count() > 0:
        for car in x:
            print(car)
    else:
        # if no results or count is 0 then tells user there are no results
        print("No results match your query")

def addCar():

    # calls input validation to check if positive number
    id = Input.getNum("Enter a car ID: ")
    reg = input("Enter car registration: ")
    # calls input validation to check if engine size a float
    engSize = Input.getFloat("Enter an engine size: ")

    # mongodb query
    car = {"_id":id ,  "car":{"reg":reg, "engineSize":engSize}}

    # mongodb inserted into db
    newCar = mycol.insert_one(car)
    # prints message to tell user record added
    print("")
    print("Record added")
    print("")
    print(car)