from pydantic import BaseModel
from datetime import datetime
from typing import Text
# Disease


class DiseaseRequest(BaseModel):
    title: str
    type: str
    body: Text
    image: str


class DiseaseResponse(BaseModel):
    title: str
    slug: str
    type: str
    excerpt: str
    body: Text
    image: str

    class Config:
        orm_mode = True


# Advice
class AdviceRequest(BaseModel):
    name: str
    email: str
    advice: str


class AdviceResponse(BaseModel):
    name: str
    email: str
    advice: str
    created_at: datetime

    class Config:
        orm_mode = True


# Predict
class PredictResponse(BaseModel):
    name: str
    slug: str
