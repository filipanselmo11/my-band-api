from app.shared.database import Base
import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, String, Integer

class MusicModel(Base):
    __tablename__ = "musicas"
    id = Column('id', UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nome = Column('nome', String, nullable=False)
    duracao = Column('duracao', Integer, nullable=False)

    