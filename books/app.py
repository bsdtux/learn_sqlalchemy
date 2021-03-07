from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import DB_URI
from models import Base, Book

# Add, Edit, Delete, Read Books
# Search Books
# Data Cleaning
# Main Loop

if __name__ == "__main__":
    engine = create_engine(DB_URI)
    Session = sessionmaker(bind=engine)
    session = Session()

    print("Engines ready to go")
    session.close()
