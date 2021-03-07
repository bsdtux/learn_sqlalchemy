import csv

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from config import DB_URI
from models import Base, Book
from utils import currency, sanitize_date


def main(session: Session) -> None:
    with open("suggested_books.csv") as infile:
        csv_reader = csv.reader(infile)
        all_books = list()
        for row in csv_reader:
            publish_date = sanitize_date(row[2])
            book = Book(title=row[0], author=row[1], publish_date=publish_date, price=currency(row[3]))
            book_in_db = session.query(Book).filter(Book.title == book.title).one_or_none()
            if book_in_db:
                print(f"Book: {book} is already in the database")
                continue
            all_books.append(book)
        session.add_all(all_books)
        session.commit()
        session.close()


if __name__ == "__main__":
    engine = create_engine(DB_URI)
    Session = sessionmaker(bind=engine)
    session = Session()

    Base.metadata.create_all(engine)
    print("Loading Books....")
    main(session)
    print("Completed seeding books database.")
