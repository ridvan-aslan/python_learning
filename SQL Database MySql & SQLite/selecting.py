import os
from dotenv import load_dotenv
import mysql.connector

load_dotenv()

db = mysql.connector.connect(
    host=os.getenv("DB_HOST"), 
    user=os.getenv("DB_USER"), 
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)

cursor = db.cursor()

def insert_product(name, price, image_url, description):
    sql = "INSERT INTO products (name, price, image_url, description) VALUES (%s, %s, %s, %s)"
    value = (name, price, image_url, description)

    try:
        cursor.execute(sql, value)
        db.commit()
        print(cursor.rowcount, "record inserted.")
        print(f"Last record id: {cursor.lastrowid}")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        
    finally:
        cursor.close()
        db.close()
        print("Database connection closed.")

def insert_products(my_list):
    sql = "INSERT INTO products (name, price, image_url, description) VALUES (%s, %s, %s, %s)"
    value = (my_list)

    try:
        cursor.executemany(sql, value)
        db.commit()
        print(cursor.rowcount, "record inserted.")
        print(f"Last record id: {cursor.lastrowid}")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        db.close()
        print("Database connection closed.")

def get_products():
    # sql = "SELECT * FROM products"
    sql = "SELECT name, price FROM products"

    try:
        cursor.execute(sql)
        # result = cursor.fetchall()
        result = cursor.fetchone()

        print(f"Name : {result[0]} Price: {result[1]}")

        # for row in result:
        #     # print(f"Name : {row[1]} Price: {row[2]}")
        #     print(f"Name : {row[0]} Price: {row[1]}")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
   
get_products()


