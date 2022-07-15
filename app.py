import sqlalchemy
from models import (Base, session, Product, engine)

import datetime
import csv


def add_csv():
    with open("inventory.csv") as csv_file:
        data = csv.reader(csv_file)
        for row in data:
            print(row)
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
    price_list = price_string.split("$")
    try:
        price_float = float(price_list.pop(1))  # Pops number off the list and converts it to a float.
    except IndexError:
        pass  # Handles exception for a text string value.
    else:
        return int(price_float * 100)  # returns price in cents.


if __name__ == "__main__":
    Base.metadata.create_all(engine)
    add_csv()
