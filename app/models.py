from datetime import datetime

from sqlalchemy import Column,Integer,String,Boolean,DateTime,Text

from .database import Base

class Note(Base):

    __tablename__ = "notes"

    id = Column(Integer,primary_key=True,index=True)
    title = Column(String(100),nullable=False)
    content = Column(Text,nullable=True)
    created_at = Column(DateTime,default=datetime.utcnow,nullable=False)
    updated_at = Column(DateTime,default=datetime.utcnow,onupdate=datetime.utcnow)