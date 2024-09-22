from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, models, schemas
from ..database import SessionLocal, engine
from typing import List

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def welcome():
    return ({"Welcome to test project"})

@router.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # Check if the user with the same email already exists
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    return crud.create_user(db=db, user=user)

@router.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.put("/update_user/{user_id}", response_model=schemas.User)
def update_user(user_id: int, user: schemas.UserUpdate, db: Session = Depends(get_db)):
    # Check if the user with the given ID exists
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    # Check if the email is already registered to another user
    email_user = db.query(models.User).filter(models.User.email == user.email).first()
    if email_user and email_user.id != user_id:
        raise HTTPException(status_code=400, detail="Email already registered")

    return crud.update_user(db=db, user_id=user_id, user_update=user)

@router.delete("/delete_user/{user_id}", response_model=schemas.User)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    return crud.delete_user(db=db, user_id=user_id)

@router.get("/all_users", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 10, is_active: bool = True, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit, is_active= is_active)
    return users


