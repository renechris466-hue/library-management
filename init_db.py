from database.db import Base
from database.db import engine

from models.book import Book
from models.transaction import Transaction
from models.employee import Employee
from models.review_queue import ReviewQueue

Base.metadata.create_all(
    bind=engine
)

print(
    "All Tables Created Successfully"
)