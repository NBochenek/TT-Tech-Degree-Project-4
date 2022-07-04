from sqlalchemy import create_engine, Column, Integer, String, Date

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine("sqlite:///inventory.db", echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Product(Base):
    __tablename__ = "Inventory"

    product_id = Column(Integer, primary_key=True)
    product_name = Column("Name", String)
    product_quantity = Column("Quantity", Integer)
    product_price = Column("Price", Integer)
    date_updated = Column("Updated", Date)


