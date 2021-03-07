from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///users.db")
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class User(Base):
    """User Model"""

    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)


if __name__ == "__main__":
    Base.metadata.create_all(engine)

    # users = [
    #     User(name="Kara Stephens", fullname="Kara Lynn Stephens", nickname=""),
    #     User(name="Abigail Stephens", fullname="Abigail Jane Stephens", nickname="AJ"),
    #     User(name="Levi Stephens", fullname="Levi Edward Stephens", nickname="nugget"),
    # ]
    # session.add_all(users)
    # session.commit()
