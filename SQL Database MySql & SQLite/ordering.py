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

    sql = "SELECT * FROM products ORDER BY name, id"

    try:
        cursor.execute(sql)
        result = cursor.fetchall()

        for row in result:
            print(f"ID: {row[0]} Name : {row[1]} Price: {row[2]}")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    
    finally:
        cursor.close()
        db.close()
        print("Database connection closed.")
   
def get_product_by_id(id):

    sql = "SELECT name, price, id FROM products WHERE id = %s"
    value = (id,)

    try:
        cursor.execute(sql, value)
        result = cursor.fetchone()
        if result:
            print(f"ID: {result[2]} Name : {result[0]} Price: {result[1]}")
        else:
            print(f"No product found with ID: {id}")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

get_products()


