from pydantic import BaseModel
from sqlalchemy import create_engine, Column, String, Integer, Engine, event, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, scoped_session

engine = create_engine("sqlite://", echo=True)
Base = declarative_base()
Session = scoped_session(sessionmaker(bind=engine))
Session.configure(bind=engine)


@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()

class Author(Base):
    __tablename__ = "author_t"

    id = Column(Integer, primary_key=True)
    firstname = Column(String)
    lastname = Column(String)

    def __repr__(self):
        return f'{self.id}, {self.firstname} {self.lastname}'


class Book(Base):
    __tablename__ = "book_t"

    id = Column(Integer, primary_key=True)
    isbn = Column(String)
    name = Column(String)
    author_id = Column(Integer, ForeignKey("author_t.id"), nullable=False)

    def __repr__(self):
        return f'{self.id}, {self.isbn}, {self.name}, {self.author_id}'


Base.metadata.create_all(engine)