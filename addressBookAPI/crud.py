from sqlalchemy.orm import Session
from sqlalchemy import func

from models import AddressBook
import schemas


def get_address_by_name(db: Session, name: str):
    return db.query(AddressBook).filter(AddressBook.name == name).first()


def get_all_address(db: Session, skip: int = 0, limit: int = 100):
    return db.query(AddressBook).offset(skip).limit(limit).all()


def create_address(db: Session, address: schemas.AddressBase):
    db_address = AddressBook(**address.dict())
    db.add(db_address)
    db.commit()
    db.refresh(db_address)
    return db_address


def delete_address_by_name(db: Session, name: str):
    try:
        db.query(AddressBook).filter(AddressBook.name == name).delete()
        db.commit()
    except Exception as e:
        raise Exception(e)


def update_address(db: Session, address: schemas.UpdateAddress, name: str):
    address_data = address.dict(exclude_unset=True)
    db.query(AddressBook).filter(AddressBook.name == name).update(address_data)
    db.commit()
    return db.query(AddressBook).filter(AddressBook.name == name).first()


# Sqlite db installed is not supporting the sin and cos function
def get_address_near_coordinates(db: Session, latitude: float, longitude: float, distance: float, skip: int = 0, limit: int = 100):
    adds = db.query(AddressBook).filter(
        (func.degrees(
            func.acos(
                func.sin(func.radians(latitude)) * func.sin(func.radians(AddressBook.latitude)) +
                func.cos(func.radians(latitude)) * func.cos(func.radians(AddressBook.latitude)) *
                func.cos(func.radians(longitude))
            )
        ) * 60 * 1.1515 * 1.609344 <= distance)
    ).all()
    return adds
