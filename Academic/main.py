# Here I want to create a main file that will run the whole project
# It should be OOP and should be able to run the whole project
# When you run it, it will print welcome message and ask you to choose a function
# Then it will run the function you choose
import sqlite3

# define a class called welcome
class Main:
    def __init__(self):
        self.conn = sqlite3.connect("users.db")
        self.create_table()

    def welcome_message(self):
        print("Welcome to the Academic Project")

    def create_table(self):
        self.conn.execute("""CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
        )""")
        self.conn.commit()

    def add_user(self):
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        self.conn.execute("INSERT INTO users (name, email) VALUES (?,?)", (name, email))
        self.conn.commit()
        print ("User added successfully")


    def function_one(self):
        print("This is function one")
    # define a function called function_one
    # Here function one is to connect to the database and store the user's information


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



# Here I want to connect the project to database, so that I can store the user's information



if __name__ == "__main__":
    main = Main()
    main.run_project()
    