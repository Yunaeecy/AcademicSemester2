import sqlite3
import hashlib
import csv

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


    def create_titanic_table(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS Titanic (
            PassengerId INTEGER,
            Survived INTEGER, -- 0 = No, 1 = Yes
            Pclass INTEGER,
            Name TEXT,
            Sex TEXT,
            Age REAL,
            SibSp INTEGER,
            Parch INTEGER,
            Ticket TEXT,
            Fare REAL,
            Cabin TEXT,
            Embarked TEXT,
            PRIMARY KEY (PassengerId)
        )''')
        self.conn.commit()
        print("Titanic table created successfully")

    def import_titanic_data(self, file_path):
        try:
            with open(file_path, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    # Check if a record with the same PassengerId already exists
                    existing_query = f'SELECT COUNT(*) FROM Titanic WHERE PassengerId={row["PassengerId"]}'
                    self.cur.execute(existing_query)
                    existing_count = self.cur.fetchone()[0]

                    if existing_count == 0:
                        # If no existing record, insert the new record
                        insert_query = '''INSERT INTO Titanic (
                            PassengerId, Survived, Pclass, Name, Sex, Age, SibSp, Parch, Ticket, Fare, Cabin, Embarked
                        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
                        self.cur.execute(insert_query, (
                            row['PassengerId'], row['Survived'], row['Pclass'], row['Name'],
                            row['Sex'], row['Age'], row['SibSp'], row['Parch'], row['Ticket'],
                            row['Fare'], row['Cabin'], row['Embarked']
                        ))
                        self.conn.commit()
        except Exception as e:
            print(f"Error importing Titanic data: {e}")

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
            