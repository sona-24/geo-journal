from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas, crud
from database import SessionLocal, engine
from typing import List
from utils import haversine
from utils import get_location_from_ip

# Create DB tables (only needed once)
# models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="GeoJournal API", version="1.0.0")

# Dependency: get DB session for request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/notes", response_model=schemas.Note)
async def create_note(note: schemas.NoteCreate, db: Session = Depends(get_db)):
    note = note.copy_mutable()  # Make it editable
    if note.latitude is None or note.longitude is None:
        coords = await get_location_from_ip()
        if coords:
            note.latitude, note.longitude = coords

    return crud.create_note(db, note)


@app.get("/notes", response_model=List[schemas.Note])
def read_notes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_notes(db, skip=skip, limit=limit)


@app.get("/notes/nearby", response_model=List[schemas.Note])
def get_nearby_notes(
    lat: float,
    lon: float,
    radius_km: float = 10,
    db: Session = Depends(get_db)
):
    all_notes = crud.get_notes(db, skip=0, limit=1000)
    nearby = []

    for note in all_notes:
        if note.latitude is None or note.longitude is None:
            continue
        distance = haversine(lat, lon, note.latitude, note.longitude)
        if distance <= radius_km:
            nearby.append(note)

    return nearby

