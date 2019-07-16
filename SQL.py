# Zoe Cahill - Applied Databases Project
# This file contains all the functions related to the SQL queries in this project
import pymysql

conn = None
# Setting up database connection
def connect():
    global conn
    conn = pymysql.connect(host="localhost", user="root", password="root", db="world", cursorclass=pymysql.cursors.DictCursor)

# Menu 1: View first 15 cities in world database
def viewCities():
    # If connect not open start it
    if(not conn):
        connect()

    # Text of SQL query
    query = "SELECT ID, Name, CountryCode, District, Population FROM city LIMIT 15"

    with conn:
        cursor = conn.cursor()
        # Connects to world database and runs out query
        cursor.execute(query)
        result = cursor.fetchall()
        # Will loop through each result and print one by one
        for x in result:
            print(x)

# Menu 2: View citties by population
def viewCitiesPop(s, num):
    # If connect not open start it
    if(not conn):
        connect()

    # Text of SQL query
    query = "SELECT ID, Name, CountryCode, District, Population FROM city WHERE Population {} {}".format(s, num)

    with conn:
        # Connecting to world database and runs query
        cursor = conn.cursor()
        row_count = cursor.execute(query)

        # Checks how many rows returned in order to give feedback on no results found
        if row_count > 0:
            result = cursor.fetchall()
            # Will loop through each result and print one by one
            for x in result:
                print(x)
        else:
            # if row_count is 0 then there were no matches to query
            print("No results match this query")

# Menu 3: Add new city
# Take 4 inputs from user tot insert
def addCity(name, code, dist, pop):
    # if not connect to db start connection
    if(not conn):
        connect()

    # SQL query for db - insert variables using .format()
    query = "INSERT INTO city (Name, CountryCode, District, Population) VALUES ('{}','{}','{}',{})".format(name, code, dist, pop)
    with conn:
        # connects to world db and executes query
        cursor = conn.cursor()
        cursor.execute(query)
        # inserts variables into database
        x = cursor.fetchall()
        return x

# Menu 6: View country by name
def countryName(string):
    # if not connect then connect to db
    if(not conn):
        connect()

    # SQL query inserts variable using .format()
    query = "SELECT Name, Continent, Population, HeadOfState FROM country WHERE name LIKE '%{}%'".format(string)

    # connects to world db
    with conn:
        cursor = conn.cursor()
        # row_count tells how many rows so can give feedback to user if no results found
        row_count = cursor.execute(query)
        
        # if there are results print them
        if row_count > 0:
            result = cursor.fetchall()
            for x in result:
                print(x)
        else:
            # if row_count 0 then tells user the are no results which match
            print("No results match this query")

# Menu 7: view country by pop
# takes 2 inputs by user
def countryPop(s, num):
    # if connection not opened to world, then open it
    if (not conn):
        connect()

    # SQL query - inserted variable using .format()
    query = "SELECT Code, Name, Continent, Population FROM country WHERE population {} {}".format(s, num)

    with conn:
        #connects to db and runs sql query
        cursor = conn.cursor()
        row_count = cursor.execute(query)

        # if row_count is more than 0 there are results so print them
        if row_count > 0:
            result = cursor.fetchall()
            for x in result:
                print(x)
        else:
            # otherwise row_count is 0 and there are no results
            print("No results match this query")