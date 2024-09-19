from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.shared.dependencies import get_db
from app.services.band_service import BandService
from app.repositories.band_repository import BandRepository
from app.schemas.band_schema import BandRequest, BandResponse
import uuid
from typing import List

router = APIRouter()

def get_band_service(db: Session = Depends(get_db)) -> BandService:
    repository = BandRepository(db)
    return BandService(repository=repository)


@router.post('/api/v1/bands', response_model=BandResponse)
def create_band(band_request: BandRequest, service: BandService = Depends(get_band_service)):
    return service.create_band(band_request=band_request)

@router.get('/api/v1/bands/{band_id}', response_model=BandResponse)
def get_band(band_id: uuid.UUID, service: BandService=Depends(get_band_service)):
    return service.get_banda(band_id=band_id)

@router.get('/api/v1/bands', response_model=List[BandResponse])
def list_bands(service: BandService = Depends(get_band_service)):
    return service.list_bands()