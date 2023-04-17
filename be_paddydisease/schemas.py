from pydantic import BaseModel
from datetime import datetime
# Disease


class DiseaseRequest(BaseModel):
    title: str
    slug: str
    type: str
    excerpt: str
    body: str
    image: str


class DiseaseResponse(BaseModel):
    title: str
    slug: str
    type: str
    excerpt: str
    body: str
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
