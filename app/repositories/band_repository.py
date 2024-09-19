from sqlalchemy.orm import Session
from app.models.band_model import BandModel
from typing import Optional, List
import uuid


class BandRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def add(self, banda: BandModel) -> BandModel:
        self.session.add(banda)
        self.session.commit()
        self.session.refresh(banda)
        return banda
    
    def get(self, banda_id: uuid.UUID) -> Optional[BandModel]:
        return self.session.query(BandModel).filter_by(id=banda_id).first()
    
    def get_all(self) -> List[BandModel]:
        return self.session.query(BandModel).all()

