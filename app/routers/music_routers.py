from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.shared.dependencies import get_db
from app.services.music_service import MusicService
from app.repositories.music_repository import MusicRepository
from app.schemas.music_schema import MusicRequest, MusicResponse
import uuid
from typing import List

router = APIRouter()

def get_music_service(db: Session = Depends(get_db)) -> MusicService:
    repository = MusicRepository(db)
    return MusicService(repository=repository)


@router.post('/api/v1/musics', response_model=MusicResponse)
def create_music(music_request: MusicRequest, service: MusicService=Depends(get_music_service)):
    return service.create_music(music_request=music_request)

@router.get('/api/v1/musics/{music_id}', response_model=MusicResponse)
def get_music(music_id: uuid.UUID, service: MusicService=Depends(get_music_service)):
    return service.get_music(music_id=music_id)

@router.get('/api/v1/musics', response_model=List[MusicResponse])
def list_musics(service: MusicService = Depends(get_music_service)):
    return service.list_musics()