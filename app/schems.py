from datetime import datetime
from pydantic import BaseModel, Field

# ----------------------------
# Umumiy schema
# ----------------------------
class NoteBase(BaseModel):
    title: str = Field(..., min_length=3, max_length=100)
    content: str | None = Field(None, max_length=500)

# ----------------------------
# Yangi note yaratishda
# ----------------------------
class NoteCreate(NoteBase):
    pass

# ----------------------------
# Note yangilaganda
# ----------------------------
class NoteUpdate(BaseModel):
    title: str | None = Field(None, min_length=3, max_length=100)
    content: str | None = Field(None, max_length=500)

# ----------------------------
# Foydalanuvchiga qaytariladigan schema
# ----------------------------
class NoteOut(NoteBase):
    id: int
    created_at: datetime
    updated_at: datetime | None

    class Config:
        from_attributes = True
