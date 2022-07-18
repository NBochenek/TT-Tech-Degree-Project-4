import sqlalchemy
from models import (Base, session, Product, engine)

import datetime
import csv


def add_csv():  # Consider adding a user prompt asking whether csv has headers.
    with open("inventory.csv") as csv_file:
        data = csv.reader(csv_file)
        next(data)  # Skips column headers in csv
        for row in data:
            product_in_db = session.query(Product).filter(Product.product_name==row[0]).one_or_none()
            if product_in_db is None:
                name = row[0]
                price = clean_price(row[1])
                quantity = row[2]
                date = clean_date(row[3])  # Indicates which row holds the date.
                new_product = Product(product_name=name, product_price=price, product_quantity=quantity, date_updated=date)
                session.add(new_product)
        session.commit()

def clean_date(date_string):
    split_date = date_string.split("/")  # Converts date string into list.
    try:
        month = int(split_date[0])  # Converts each item in list to integer.
        day = int(split_date[1])
        year = int(split_date[2])
        return datetime.date(year, month, day)  # Returns each integer as datetime value.
    except ValueError:  # Excepts non-date string value.
        pass

def clean_price(price_string):
    try:
        price_float = float(price_string.split("$")[1])
        return int(price_float * 100)  # returns price in cents.
    except IndexError:
        print(
            "Invalid entry. Please enter a number in the format '$00.00'")  # Handles exception for a value without $.
        return
    except ValueError:
        print("Invalid entry. Please enter a number in the format '$00.00'") # Handles exception for a text string value.
        return
  # How could I code this as to not require a $?

def menu():
    while True:
        print("Please select from the following options:\n\n"
              "v - Select a product from the database.\n"
              "a - Add a product to the database.\n"
              "b - Create a backup of the database.\n"
              "x - Exit the program.\n")
        options = ["v", "a", "b", "x"]
        choice = input("Please make a selection:\n").lower()
        if choice in options:
            return choice
        else:
            input("Error! Please make a valid selection.")


def app():
    app_running = True
    while app_running:
        choice = menu()
        if choice == "v":  # Select product
            pass
        elif choice == "a":  # Add product
            name = input("Enter product name:\n")
            price_error = True  # Creates loop to ensure user enters valid integer.
            while price_error:
                price = input("Enter product price:\n")
                price = clean_price(price)
                if type(price) is int:
                    price_error = False
            quantity_error = True
            while quantity_error:
                quantity = input("Enter product quantity:\n")
                if type(quantity) is int:
                    quantity_error = False
                else:
                    print("Please enter quantity as an integer.")
            date = datetime.datetime.now()
        elif choice == "b":  # Backup database
            pass
        else:
            print("Thank you for using the database app!")

if __name__ == "__main__":
    # Base.metadata.create_all(engine)
    # add_csv()
    app()
