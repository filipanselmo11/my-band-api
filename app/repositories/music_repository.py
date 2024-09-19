from sqlalchemy.orm import Session
from app.models.music_model import MusicModel
from typing import Optional, List
import uuid

class MusicRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def add(self, music: MusicModel) -> MusicModel:
        self.session.add(music)
        self.session.commit()
        self.session.refresh(music)
        
        return music
    
    def get(self, music_id: uuid.UUID) -> Optional[MusicModel]:
        return self.session.query(MusicModel).filter_by(id=music_id).first()
    
    def get_all(self) -> List[MusicModel]:
        return self.session.query(MusicModel).all()