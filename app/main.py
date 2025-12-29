from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .database import engine, get_db
from . import models, schemas, crud

app = FastAPI(title="My FastAPI App")

@app.get("/")
def root():
    return {"message": "FastAPI is running"}

@app.post("/users", response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)

@app.get("/users", response_model=list[schemas.UserResponse])
def read_users(db: Session = Depends(get_db)):
    return crud.get_users(db)
