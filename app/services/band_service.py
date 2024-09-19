from app.repositories.band_repository import BandRepository
from app.schemas.band_schema import BandRequest, BandResponse
from app.models.band_model import BandModel
from typing import Optional, List
import uuid


class BandService:
    def __init__(self, repository: BandRepository):
        self.repository = repository

    def create_band(self, band_request: BandRequest) -> BandResponse:
        banda = BandModel(**band_request.model_dump())
        banda = self.repository.add(banda)
        return BandResponse.model_validate(banda)
    
    def get_band(self, banda_id: uuid.UUID) -> Optional[BandResponse]:
        banda = self.repository.get(banda_id)
        return BandResponse.model_validate(banda) if banda else None
    
    def list_bands(self) -> List[BandResponse]:
        bandas = self.repository.get_all()
        return [BandResponse.model_validate(banda) for banda in bandas]