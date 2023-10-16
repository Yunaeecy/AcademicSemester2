import sqlite3

class TableCreator:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cur = self.conn.cursor()

    def create_user_table(self):
        self.cur.execute("CREATE TABLE users(id, name, email)")
        self.conn.commit()
        print("User table created successfully")

    def close_connection(self):
        self.cur.close()
        self.conn.close()

if __name__ == "__main__":
    #specify the database name
    db_name = "academic.sqlite"
    #create an instance of TableCreator
    table_creator = TableCreator(db_name)
    #call the method to create the user table
    table_creator.create_user_table()
    #close the connection
    table_creator.close_connection()
    