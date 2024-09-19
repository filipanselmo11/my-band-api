from app.repositories.music_repository import MusicRepository
from app.schemas.music_schema import MusicRequest, MusicResponse
from app.models.music_model import MusicModel
import uuid
from typing import Optional, List

class MusicService:
    def __init__(self, repository: MusicRepository):
        self.repository = repository

    def create_music(self, music_request: MusicRequest) -> MusicResponse:
        music = MusicModel(**music_request.model_dump())
        music = self.repository.add(music=music)
        return MusicResponse.model_validate(music)
    
    def get_band(self, music_id: uuid.UUID) -> Optional[MusicResponse]:
        music = self.repository.get(music_id=music_id)
        return MusicResponse.model_validate(music) if music else None
    
    def list_musics(self) -> List[MusicResponse]:
        musics = self.repository.get_all()
        return [MusicResponse.model_validate(music) for music in musics]

