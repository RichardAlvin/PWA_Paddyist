from sqlalchemy.orm import Session
import models
import schemas


# def create_disease(db: Session, disease: schemas.DiseaseRequest):
#     db_todo = models.Disease(name=disease.name, completed=disease.completed)
#     db.add(db_todo)
#     db.commit()
#     db.refresh(db_todo)
#     return db_todo


def read_disease(db: Session):
    return db.query(models.Disease).all()


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


# def delete_todo(db: Session, id: int):
#     db_todo = db.query(models.ToDo).filter(models.ToDo.id == id).first()
#     if db_todo is None:
#         return None
#     db.query(models.ToDo).filter(models.ToDo.id == id).delete()
#     db.commit()
#     return True
