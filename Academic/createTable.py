import sqlite3
import hashlib

class TableCreator:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cur = self.conn.cursor()

    def create_user_table(self):
        create_table_query = """
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            email TEXT NOT NULL
        );   

"""
        self.cur.execute(create_table_query)
        self.conn.commit()
        print("User table created successfully")

    def close_connection(self):
        self.cur.close()
        self.conn.close()

    def hash_password(self, password):
        # hash the password
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        return hashed_password
    
    def register_user(self):
        print("=== Registration ===")
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        email = input("Enter your email: ")

        # insert the user into the database
        try:
            # hash the password
            hashed_password = self.hash_password(password)
            insert_user_query = "INSERT INTO users (username, password, email) VALUES (?,?,?)"
            self.cur.execute(insert_user_query, (username, hashed_password, email))
            self.conn.commit()
            print ("User registered successfully")
        except sqlite3.IntegrityError:
            print("Error: Username is not unique. Please choose a different username.")

    def login_user(self):
        print("=== Login ===")
        input_username = input("Enter your username: ")
        input_password = input("Enter your password: ")
        # hash the password
        hashed_password = self.hash_password(input_password)
        select_user_query = "SELECT * FROM users WHERE username=? AND password=?"
        self.cur.execute(select_user_query, (input_username, hashed_password))
        user_data = self.cur.fetchone()
        
        if user_data:
            print("Login successfully")
            return user_data
        
        else:
            print("Error: Username or password is incorrect. Please try again.")
            return None
            