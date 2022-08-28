from pydoc import describe
from turtle import title
from sqlalchemy import Column, Integer, String, Float

from database import Base


class AddressBook(Base):
    '''
        Model to store Address with name, contact, email, text address, latitude and longitude in degree
    '''
    __tablename__ = "addressBook"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(60), index=True, unique=True)
    contact = Column(Integer, index=True)
    email = Column(String(60), index=True)
    address = Column(String, index=True)
    latitude = Column(Float, index=True)
    longitude = Column(Float, index=True)
