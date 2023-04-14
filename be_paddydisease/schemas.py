from pydantic import BaseModel


class DiseaseRequest(BaseModel):
    name: str
    completed: bool


class DiseaseResponse(BaseModel):
    name: str
    completed: bool
    id: int

    class Config:
        orm_mode = True
