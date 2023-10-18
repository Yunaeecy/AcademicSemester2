
import sqlite3
import requests

from createTable import TableCreator

# define a class called Main
class Main:
    def __init__(self):
        # specify the database name
        self.db_name = "academic.sqlite"
        # create an instance of TableCreator
        self.table_creator = TableCreator(self.db_name)
        # create the user table
        self.table_creator.create_user_table()

        # create the titanic table and import the data from the CSV file of local machine   
        self.table_creator.create_titanic_table()
        self.table_creator.import_titanic_data("/Users/yuna/Downloads/titanic/train.csv")


        # iniitialize database connection variables
        self.conn = sqlite3.connect(self.db_name)
        self.cur = self.conn.cursor()
        print ("Database connection established")

        self.table_creator.register_user()
        self.table_creator.login_user()
        # close the connection
        self.table_creator.close_connection()

        
        # initialize the logged in user
        self.logged_in_user = None


    def register_user(self):
        while True:
            success = self.table_creator.register_user()
            if success:
                break

    def login_user(self):
        while True:
            user_data = self.table_creator.login_user()
            if user_data:
                self.logged_in_user = user_data
                break



    def welcome_message(self):
        print("Welcome to the Academic Project")


    def search_titanic_data(self):
        print("=== Search Titanic Data ===")
        age_range_start = float(input("Enter the start of age range: "))
        age_range_end = float(input("Enter the end of age range: "))

        query = f"""
        SELECT COUNT(*) FROM Titanic
        WHERE Age >= {age_range_start} AND Age <= {age_range_end}
        """
        self.cur.execute(query)
        result = self.cur.fetchone()

        print(f"Number of people survived between {age_range_start} and {age_range_end} is {result[0]}")


    def function_one(self):
        pass
    
        


    def function_two(self):
        print("This is function two")

    def run_project(self):
        self.welcome_message()
        while True:
            choice = input("Choose a function (1,2,or q to quit):  ")
            if choice == "1":
                self.search_titanic_data()
            elif choice == "2":
                self.function_two()
            elif choice == "q":
                break
            else:
                print("Invalid choice, please try again")

if __name__ == "__main__":
    main = Main()
    main.run_project()
    