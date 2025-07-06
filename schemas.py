from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class NoteBase(BaseModel):
    title: str = Field(..., example="Hike to the cliffs")
    content: str = Field(..., example="Saw an eagle flying over the valley.")
    latitude: Optional[float] = Field(None, example=37.7749)
    longitude: Optional[float] = Field(None, example=-122.4194)
    tags: Optional[str] = Field(None, example="hiking,nature,california")

class NoteCreate(NoteBase):
    def copy_mutable(self):
        return self.model_copy(update={})


class Note(NoteBase):
    id: int
    created_at: datetime

    class Config:
        model_config = {"from_attributes": True}
