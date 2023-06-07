from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status
import schemas
import crud
from database import SessionLocal
from fastapi import File, UploadFile
import sys

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
    try:
        disease = crud.create_disease(db, disease)
        if disease == False:
            return "Title already exist, please use another Title!"
        return "berhasil"
    except:
        e = sys.exc_info()[1]
        raise HTTPException(status_code=500, detail=str(e))


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


@router.get("/{slug}")
def get_disease_by_slug(slug: str, db: Session = Depends(get_db)):
    disease = crud.read_disease_by_slug(db, slug)
    if disease is None:
        raise HTTPException(status_code=404, detail="Disease not found")
    return disease


@router.put("/{id}")
def update_disease(id: int, disease: schemas.DiseaseRequest, db: Session = Depends(get_db)):
    disease = crud.update_disease(db, id, disease)
    if disease is None:
        raise HTTPException(status_code=404, detail="Disease not found")
    return disease
