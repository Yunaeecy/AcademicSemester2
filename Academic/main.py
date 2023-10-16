# Here I want to create a main file that will run the whole project
# It should be OOP and should be able to run the whole project
# When you run it, it will print welcome message and ask you to choose a function
# Then it will run the function you choose
import sqlite3
from createTable import TableCreator

# define a class called Main
class Main:
    def __init__(self):
        # # connect to the database and create a cursor
        # self.conn = sqlite3.connect("academic.sqlite")
        # self.cur = self.conn.cursor()
        # # self.cur.execute("CREATE TABLE users(id, name, email)")
        # # self.conn.commit()
        # # write a query and execute it with the cursor
        # self.query = "select sqlite_version();"
        # self.cur.execute(self.query)
        # # fetch and output the result
        # self.result = self.cur.fetchone()
        # print("SQLite version: {}".format(self.result))
        # # close the cursor and connection
        # self.cur.close()

        # create an instance of TableCreator
        table_creator = TableCreator("academic.sqlite")
        table_creator.create_user_table()
        table_creator.close_connection()

        # initialize database connection variables
        self.conn = None
        self.cur = None



    def welcome_message(self):
        print("Welcome to the Academic Project")


    def add_user(self):
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        self.conn.execute("INSERT INTO users (name, email) VALUES (?,?)", (name, email))
        self.conn.commit()
        print ("User added successfully")


    def function_one(self):
    # Here function one is to connect to the database
        connect_to_db = input("Do you want to connect to the database? (y/n): ").lower()
        if connect_to_db == "y":
            # connect to the database
            self.conn = sqlite3.connect("academic.sqlite")
            self.cur = self.conn.cursor()
            print ("Connected to the database")
        else:
            print ("Not connected to the database")
    
        


    def function_two(self):
        print("This is function two")

    def run_project(self):
        self.welcome_message()
        while True:
            choice = input("Choose a function (1,2,or q to quit):  ")
            if choice == "1":
                self.function_one()
            elif choice == "2":
                self.function_two()
            elif choice == "q":
                break
            else:
                print("Invalid choice, please try again")

if __name__ == "__main__":
    main = Main()
    main.run_project()
    