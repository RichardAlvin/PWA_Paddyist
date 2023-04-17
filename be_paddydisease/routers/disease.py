from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status
import schemas
import crud
from database import SessionLocal

router = APIRouter(
    prefix="/disease"
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("", status_code=status.HTTP_201_CREATED)
def create_disease(disease: schemas.DiseaseRequest, db: Session = Depends(get_db)):
    disease = crud.create_disease(db, disease)
    return disease


@router.get("", response_model=List[schemas.DiseaseResponse])
def get_diseases(db: Session = Depends(get_db)):
    diseases = crud.read_disease(db)
    return diseases


@router.delete("/{id}", status_code=status.HTTP_200_OK)
def delete_disease(id: int, db: Session = Depends(get_db)):
    res = crud.delete_disease(db, id)
    if res is None:
        raise HTTPException(status_code=404, detail="Disease not found")
    else:
        return {"message": "Successfull Delete Disease!"}


# @router.get("/{id}")
# def get_todo_by_id(id: int, db: Session = Depends(get_db)):
#     todo = crud.read_todo(db, id)
#     if todo is None:
#         raise HTTPException(status_code=404, detail="to do not found")
#     return todo


# @router.put("/{id}")
# def update_todo(id: int, todo: schemas.ToDoRequest, db: Session = Depends(get_db)):
#     todo = crud.update_todo(db, id, todo)
#     if todo is None:
#         raise HTTPException(status_code=404, detail="to do not found")
#     return todo
