import uuid
from .base import Base
from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, String, Integer, DateTime


class Book(Base):
    __tablename__ = "books"
    id = Column(
        UUID(as_uuid=True),
        unique=True,
        primary_key=True,
        default=uuid.uuid4,
        nullable=False,
    )
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    year = Column(Integer, default=None)
    genre = Column(String, default=None)
    publication = Column(String, default=None)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    def __ref___(self):
        return f"<Book(title='{self.title}', author='{self.author}')>"
