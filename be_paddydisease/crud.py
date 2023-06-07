from sqlalchemy.orm import Session
from datetime import datetime
import models
import schemas


def create_disease(db: Session, disease: schemas.DiseaseRequest):
    slug = disease.title.replace(" ", "_").lower()
    excerpt = generate_excerpt(disease.body)

    # check excerpt in disease table (must unique)
    check_slug = db.query(models.Disease).filter(
        models.Disease.slug == slug).first()

    if check_slug is not None:
        return False

    # save new disease to table
    db_disease = models.Disease(title=disease.title, slug=slug, type=disease.type,
                                excerpt=excerpt, body=disease.body, image=disease.image)
    db.add(db_disease)
    db.commit()
    db.refresh(db_disease)
    return db_disease


def generate_excerpt(text, max_length=100):
    if len(text) <= max_length:
        return text
    else:
        return text[:max_length] + "..."


def read_disease(db: Session):
    return db.query(models.Disease).all()


def read_disease_by_slug(db: Session, slug: str):
    return db.query(models.Disease).filter(models.Disease.slug == slug).first()


def update_disease(db: Session, id: int, disease: schemas.DiseaseRequest):
    db_disease = db.query(models.Disease).filter(
        models.Disease.id == id).first()
    if db_disease is None:
        return None
    db.query(models.Disease).filter(models.Disease.id == id).update(
        {'title': disease.title, 'slug': disease.slug, 'type': disease.type, 'excerpt': disease.excerpt, 'body': disease.body, 'image': disease.image})
    db.commit()
    db.refresh(db_disease)
    return db_disease


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
