from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import band_routers
from app.routers import music_routers

app = FastAPI()

origins = [
    "http://localhost"
]

@app.get('/')
async def root():
    return "Salve guys !"

app.include_router(band_routers.router)
app.include_router(music_routers.router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=['*'],
    allow_headers=['*']
)