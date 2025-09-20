from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session

from ..import models,schems
from ..dependencies import get_db

router = APIRouter(
    prefix="/notes",
    tags=["Notes"]
)

# Yangi note yaratish

@router.post("/",response_model=schems.NoteOut,status_code=status.HTTP_404_NOT_FOUND)
def create_note(note:schems.NoteCreate,db: Session = Depends(get_db)):
    db_note = models.Note(**note.dict())
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note

# Barcha notelarni olish
@router.get("/",response_model=list[schems.NoteOut])
def get_notes(db:Session = Depends(get_db)):
    return db.query(models.Note).all()


# Bitta note olish

@router.get("/{note_id}",response_model = schems.NoteOut)
def get_one(note_id:int,db:Session = Depends(get_db)):
    db_note  = db.query(models.Note).filter(models.Note.id == note_id).first()
    if not db_note:
        raise HTTPException(status_code=404,detail="Note not found")
    return db_note

# Note YAngilash
@router.put("/{note_id}",response_model=schems.NoteOut)
def update_note(note_id:int,update_note:schems.NoteUpdate,db:Session = Depends(get_db)):
    db_note = db.query(models.Note).filter(models.Note.id == note_id).first()
    if not db_note:
        raise HTTPException(status_code=404, detail="Note not found")
    
    for key,value in update_note.dict(exclude_unset=True).items():
        setattr(db_note,key,value)
    
    db.commit()
    db.refresh(db_note)
    return db_note

# Note O'chirish

@router.delete("/{note_id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_note(note_id:int,db: Session = Depends(get_db)):
    db_note = db.query(models.Note).filter(models.Note.id == note_id).first()
    if not db_note:
        raise HTTPException(status_code=404, detail="Note not found")
    db.delete(db_note)
    db.commit()
    return None