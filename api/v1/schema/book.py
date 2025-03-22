from typing import Optional
from pydantic import BaseModel

class BookProps(BaseModel):
  year: Optional[int] = None
  genre: Optional[str] = None
  publication: Optional[str] = None

class Book(BookProps):
  title: str
  author: str

class BookUpdate(BookProps):
  title: Optional[str] = None
  author: Optional[str] = None
