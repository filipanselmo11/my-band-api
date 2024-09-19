from pydantic import BaseModel
import uuid

class MusicRequest(BaseModel):
    nome: str
    duracao: int

class MusicResponse(BaseModel):
    id: uuid.UUID
    nome: str
    duracao: int

    class Config:
        from_attributes = True