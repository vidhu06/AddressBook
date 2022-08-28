
from pydantic import BaseModel, validator


class AddressBase(BaseModel):
    contact: int = None
    email: str = None
    address: str
    latitude: float
    longitude: float

    @validator('latitude')
    def latitude_validation(cls, lat):
        if lat < -90 or lat > 90:
            raise ValueError('Latitude must be in range of -90 and 90')
        return lat

    @validator('longitude')
    def longitude_validation(cls, long):
        if long < -180 or long > 180:
            raise ValueError('Longitude must be in range of -180 and 180')
        return long


class Address(AddressBase):
    name: str

    class Config:
        orm_mode = True


class UpdateAddress(AddressBase):
    contact: int = None
    email: str = None
    address: str = None
    latitude: float = None
    longitude: float = None

    class Config:
        orm_mode = True
