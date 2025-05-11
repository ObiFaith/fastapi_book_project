from uuid import UUID
from api.db.database import get_session
from api.v1.services.book import BookService
from fastapi import status, APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from api.v1.schemas.book import Book, BookUpdate
from api.utils.response import success_response, error_response

book = APIRouter(prefix="/books", tags=["Book"])


@book.get("/")
async def get_books(db: AsyncSession = Depends(get_session)):
    """Get all books"""
    data = await BookService.get_books(db)
    return success_response(
        data=data,
        status_code=status.HTTP_200_OK,
        message="Book(s) retrieved successfully!",
    )


@book.get("/{book_id}")
async def get_book(book_id: UUID, db: AsyncSession = Depends(get_session)):
    """Get a book by id"""
    data = await BookService.get_book(db, book_id)

    if data is None:
        return error_response(
            message="Book not found!",
            status_code=status.HTTP_404_NOT_FOUND,
        )

    return success_response(
        data=data,
        status_code=status.HTTP_200_OK,
        message="Book retrieved successfully!",
    )


@book.post("/")
async def create_book(new_book: Book, db: AsyncSession = Depends(get_session)):
    """Add a new book"""
    data = await BookService.create_book(db, new_book)

    return success_response(
        data=data,
        status_code=status.HTTP_201_CREATED,
        message="Books retrieved successfully!",
    )


@book.put("/{book_id}")
async def update_book(
    book_id: UUID, book: BookUpdate, db: AsyncSession = Depends(get_session)
):
    book = await BookService.update_book(db, book_id, book)

    if book is None:
        error_response(
            message="Book not found!",
            status_code=status.HTTP_404_NOT_FOUND,
        )

    return success_response(
        data=book,
        status_code=status.HTTP_200_OK,
        message="Book updated successfully!",
    )


@book.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: UUID, db: AsyncSession = Depends(get_session)):
    book = await BookService.delete_book(db, book_id)

    if book is None:
        return error_response(
            message="Book not found!",
            status_code=status.HTTP_404_NOT_FOUND,
        )
