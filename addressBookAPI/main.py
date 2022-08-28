import models
import crud
import schemas
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine


app = FastAPI()

models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def read_root():
    return {"Message": "Welcome to the address Book"}


@app.get("/address/", response_model=list[schemas.Address])
def read_all_address(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    address = crud.get_all_address(db, skip=skip, limit=limit)
    return address


@app.get("/address_near_coordinates", response_model=list[schemas.Address])
def read_address_near_coordinates(latitude: float, longitude: float, distance: float, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    address = crud.get_address_near_coordinates(
        db, skip=skip, limit=limit, latitude=latitude, longitude=longitude, distance=distance)
    return address


@app.post("/address/", response_model=schemas.Address)
def create_address(address: schemas.Address, db: Session = Depends(get_db)):
    address_name = crud.get_address_by_name(db, name=address.name)
    if address_name:
        raise HTTPException(
            status_code=400, detail="Address with name {}  already registered".format(address.name))
    return crud.create_address(db=db, address=address)


@app.delete('/address/{name}')
def delete_address_by_name(name: str, db: Session = Depends(get_db)):
    address_name = crud.get_address_by_name(db, name=name)
    if not address_name:
        raise HTTPException(
            status_code=404, detail="Address with name {} does not exist".format(name))

    try:
        crud.delete_address_by_name(db=db, name=name)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Unable to delete: {e}")
    return {"delete status": "success"}


@app.patch("/address/{name}", response_model=schemas.Address)
def update_address(name: str, address: schemas.UpdateAddress, db: Session = Depends(get_db)):
    address_name = crud.get_address_by_name(db, name=name)
    if not address_name:
        raise HTTPException(
            status_code=400, detail="Address with name {}  does not exist".format(name))
    return crud.update_address(db=db, address=address, name=name)
