from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status
import schemas
import crud
from database import SessionLocal

router = APIRouter(
    prefix="/advice"
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("", status_code=status.HTTP_201_CREATED)
def create_advice(advice: schemas.AdviceRequest, db: Session = Depends(get_db)):
    advice = crud.create_advice(db, advice)
    return advice


@router.get("", response_model=List[schemas.AdviceResponse])
def get_advices(db: Session = Depends(get_db)):
    advices = crud.read_advice(db)
    return advices


@router.delete("/{id}", status_code=status.HTTP_200_OK)
def delete_advice(id: int, db: Session = Depends(get_db)):
    res = crud.delete_advice(db, id)
    if res is None:
        raise HTTPException(status_code=404, detail="Advice not found")
    else:
        return {"message": "Successfull Delete Advice!"}
