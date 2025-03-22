from fastapi import status, APIRouter
from api.v1.schema.book import Book, BookUpdate
from api.utils.responses import success_response, error_response

book = APIRouter(prefix='/books', tags=['Book'])

books = {
  1: Book(
      year=2021,
      genre='Business',
      title='Good To Great',
      author='Jim Collins',
      publication='HarperCollins'
    )
}

@book.get('/', response_model=list[Book])
async def get_books():
  """ Get all books """
  data = [
    {"id": book_id, **book.model_dump()} for book_id, book in books.items()
  ]

  return success_response(
    data=data,
    status_code=status.HTTP_200_OK,
    message="Books retrieved successfully!",
  )

@book.get('/{book_id}', response_model=Book)
async def get_book(book_id: int):
  """ Get a book by id """
  if book_id not in books:
    error_response(
      message="Book not found!",
      status_code=status.HTTP_404_NOT_FOUND,
    )

  book = books[book_id]
  data = {"id": book_id, **book.model_dump()}

  return success_response(
    data=data,
    status_code=status.HTTP_200_OK,
    message="Book retrieved successfully!",
  )

@book.post('/', response_model=Book)
async def create_book(book: Book):
  """ Add a new book """
  new_id = max(books.keys(), default=0) + 1

  books[new_id] = book
  data = {"id": new_id, **book.model_dump()}

  return success_response(
    data=data,
    status_code=status.HTTP_201_CREATED,
    message="Books retrieved successfully!",
  )

@book.put('/{book_id}', response_model=Book)
async def update_book(book_id: int, book: BookUpdate):
  if book_id not in books:
    error_response(
      message="Book not found!",
      status_code=status.HTTP_404_NOT_FOUND,
    )

  updated_book = book.model_dump(exclude_unset=True)
  books[book_id] = books[book_id].model_copy(update=updated_book)

  return success_response(
    data=books[book_id],
    status_code=status.HTTP_200_OK,
    message="Book updated successfully!",
  )

@book.delete('/{book_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int):
  if book_id not in books:
    error_response(
      message="Book not found!",
      status_code=status.HTTP_404_NOT_FOUND,
    )

  del books[book_id]
