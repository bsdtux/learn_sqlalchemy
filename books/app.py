from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from config import DB_URI
from models import Book
from utils import currency, sanitize_date


def add_book(session: Session):
    title = input("Title: ")
    author = input("Author: ")

    publish_date = None
    while not publish_date:
        publish_date = sanitize_date(input("Date(Ex: October 25, 2017): "))

    price = None
    while not price:
        price = currency(input("Price(Ex: 20.99): "))

    new_book = Book(title=title, author=author, publish_date=publish_date, price=price)
    session.add(new_book)
    session.commit()
    print(f"Book: {new_book} added")


def get_all_books(session: Session):
    for book in session.query(Book):
        print(f"{book.id} | {book.title} | {book.author}")

    input("\nPress Enter to return to main menu.")


def search_book(session: Session):
    print("Searching for book")


def analyise_book(session: Session):
    print("Analysing book")


def app(session: Session):
    app_running = True
    menu_func = {1: add_book, 2: get_all_books, 3: search_book, 4: analyise_book}
    while app_running:
        choice = menu()
        if choice == 5:
            app_running = False
            continue

        menu_func[choice](session)


def menu():
    while True:
        print(
            """===== Programming Books =====
        \r1) Add Book
        \r2) View all books
        \r3) Search For book
        \r4) Book Analysis
        \r5) quit"""
        )

        try:
            print(" ")
            choice = int(input(">>> "))
            if choice not in range(1, 6):
                raise ValueError()
            return choice
        except ValueError:
            print("Invalid choice. Choose a number from the options above.")


# Add, Edit, Delete, Read Books
# Search Books
# Data Cleaning
# Main Loop

if __name__ == "__main__":
    engine = create_engine(DB_URI)
    Session = sessionmaker(bind=engine)
    session = Session()

    app(session)
    session.close()
