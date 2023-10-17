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
    
    def add_user(self, username, password, email):
        # hash the password
        hashed_password = self.hash_password(password)
        # insert the user into the database
        try:
            insert_user_query = "INSERT INTO users (username, password, email) VALUES (?,?,?)"
            self.cur.execute(insert_user_query, (username, hashed_password, email))
            self.conn.commit()
            print ("User added successfully")
        except sqlite3.IntegrityError:
            print("Error: Username is not unique. Please choose a different username.")
            

if __name__ == "__main__":
    #specify the database name
    db_name = "academic.sqlite"
    #create an instance of TableCreator
    table_creator = TableCreator(db_name)
    #call the method to create the user table
    # table_creator.create_user_table()

    #add a user("maggie", "1234", "shengyuanmaggie@gmail.com")
    table_creator.add_user("maggie", "1234", "shengyuanmaggie@gmail.com")
    table_creator.add_user("yuna", "1234", "yunaeecy@gmail.com")

        #close the connection
    table_creator.close_connection()