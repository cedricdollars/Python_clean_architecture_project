#coding:utf-8
import sqlite3

class Database:
    dbName:str = "parking_project"
    
    def connect(self):
        try:
            sqlConn = sqlite3.connect(Database.dbName)
            cursor = sqlConn.cursor()
            print("Database created and successfully connected")
        except sqlite3 as Error:
            print('Error while connecting : ', Error)
        finally:
            if(sqlConn):
                sqlConn.close()
                print("Connection closed")
    
    def create_table(self, query):
        conn = sqlite3.connect(self.dbName)
        cursor = conn.cursor()
        cursor.execute(query)
    
   