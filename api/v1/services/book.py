from uuid import UUID
from sqlmodel import select
from sqlalchemy.ext.asyncio import AsyncSession
from api.v1.models.book import Book as BookModel
from api.v1.schemas.book import Book as BookSchema, BookUpdate


class BookService:
    """Book Functionality"""

    @staticmethod
    async def create_book(db: AsyncSession, book: BookSchema):
        book_create = BookModel(**book.model_dump())

        db.add(book_create)
        await db.commit()
        await db.refresh(book_create)
        return book_create

    @staticmethod
    async def get_books(db: AsyncSession):
        """Get All Books"""
        result = await db.execute(select(BookModel))
        return result.scalars().all()

    @staticmethod
    async def get_book(db: AsyncSession, book_id: UUID):
        """Get book by book_id"""
        result = await db.execute(select(BookModel).where(BookModel.id == book_id))
        book = result.scalar_one_or_none()
        return book

    @staticmethod
    async def update_book(db: AsyncSession, book_id: UUID, book_data: BookUpdate):
        """Get book by book_id"""
        result = await db.execute(select(BookModel).where(BookModel.id == book_id))
        book = result.scalar_one_or_none()

        if not book:
            return None

        for key, value in book_data.model_dump(exclude_unset=True).items():
            setattr(book, key, value)

        await db.commit()
        await db.refresh(book)
        return book

    @staticmethod
    async def delete_book(db: AsyncSession, book_id: UUID):
        """Delete book by book_id"""
        result = await db.execute(select(BookModel).where(BookModel.id == book_id))
        book = result.scalar_one_or_none()

        if not book:
            return None

        await db.delete(book)
        await db.commit()
