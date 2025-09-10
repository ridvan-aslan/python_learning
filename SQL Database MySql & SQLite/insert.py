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

my_list = []        

while True:
    name = input("Enter product name: ")
    price = int(input("Enter product price: "))
    image_url = input("Enter product image URL: ")
    description = input("Enter product description: ")

    my_list.append((name, price, image_url, description))

    choice = input("Do you want to add another product? (yes/no): ").lower()
    if choice != 'yes':
        print("Sending data to the database...")
        insert_products(my_list)
        print("Data sent to the database.")
        break



