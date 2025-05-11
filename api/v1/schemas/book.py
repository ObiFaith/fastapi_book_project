from typing import Optional
from pydantic import BaseModel


class BookProp(BaseModel):
    year: Optional[int] = None
    genre: Optional[str] = None
    publication: Optional[str] = None


class Book(BookProp):
    title: str
    author: str


class BookUpdate(BookProp):
    title: Optional[str] = None
    author: Optional[str] = None
