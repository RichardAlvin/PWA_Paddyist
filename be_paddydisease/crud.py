from sqlalchemy.orm import Session
from datetime import datetime
import models
import schemas


def create_disease(db: Session, disease: schemas.DiseaseRequest):
    db_disease = models.Disease(title=disease.title, slug=disease.slug, type=disease.type,
                                excerpt=disease.excerpt, body=disease.body, image=disease.image)
    db.add(db_disease)
    db.commit()
    db.refresh(db_disease)
    return db_disease


def read_disease(db: Session):
    return db.query(models.Disease).all()


def delete_disease(db: Session, id: int):
    db_disease = db.query(models.Disease).filter(
        models.Disease.id == id).first()
    if db_disease is None:
        return None
    db.query(models.Disease).filter(
        models.Disease.id == id).delete()
    db.commit()
    return True


# advice
def create_advice(db: Session, advice: schemas.AdviceRequest):
    db_advice = models.Advice(
        name=advice.name, email=advice.email, advice=advice.advice, created_at=datetime.now())
    db.add(db_advice)
    db.commit()
    db.refresh(db_advice)
    return db_advice


def read_advice(db: Session):
    return db.query(models.Advice).all()


def delete_advice(db: Session, id: int):
    db_advice = db.query(models.Advice).filter(
        models.Advice.id == id).first()
    if db_advice is None:
        return None
    db.query(models.Advice).filter(
        models.Advice.id == id).delete()
    db.commit()
    return True

# def read_todo(db: Session, id: int):
#     return db.query(models.Disease).filter(models.ToDo.id == id).first()


# def update_todo(db: Session, id: int, todo: schemas.ToDoRequest):
#     db_todo = db.query(models.ToDo).filter(models.ToDo.id == id).first()
#     if db_todo is None:
#         return None
#     db.query(models.ToDo).filter(models.ToDo.id == id).update(
#         {'name': todo.name, 'completed': todo.completed})
#     db.commit()
#     db.refresh(db_todo)
#     return db_todo
