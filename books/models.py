from sqlalchemy import Column, Date, Integer, Numeric, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    publish_date = Column(Date)
    price = Column(Numeric)

    def __repr__(self):
        return f"<Book(title={self.title}, author={self.author}, publish_date={self.publish_date}, price={self.price}>)"
