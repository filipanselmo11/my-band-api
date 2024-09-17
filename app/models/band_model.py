from app.shared.database import Base
import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, String

class BandModel(Base):
    __tablename__ = "bandas"
    id = Column('id', UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nome = Column('nome', String, nullable=False)
    genero = Column('genero', String, nullable=False)
    img = Column('img', String, nullable=False)