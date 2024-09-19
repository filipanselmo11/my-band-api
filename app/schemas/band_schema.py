from pydantic import BaseModel
import uuid

class BandRequest(BaseModel):
    nome: str
    genero: str
    img: str

class BandResponse(BaseModel):
    id: uuid.UUID
    nome: str
    genero: str
    img: str

    class Config:
        from_attributes = True