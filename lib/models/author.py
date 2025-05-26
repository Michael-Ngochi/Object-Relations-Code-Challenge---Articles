from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, validates
from db import Base
from models.article import Article  

class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique=True)

    # Relationship: One author can write many articles
    articles = relationship("Article", back_populates="author", cascade="all, delete")

    def __init__(self, name):
        self.name = name

    @validates("name")
    def validate_name(self, key, value):
        if not value or not value.strip():
            raise ValueError("Author name cannot be empty.")
        return value.strip()

    def __repr__(self):
        return f"<Author(id={self.id}, name='{self.name}')>"

    # --- SQL Methods ---
    @classmethod
    def save(cls, session, name):
        author = cls(name=name)
        session.add(author)
        session.commit()
        return author

    @classmethod
    def find_by_id(cls, session, author_id):
        return session.query(cls).filter_by(id=author_id).first()

    @classmethod
    def find_by_name(cls, session, name):
        return session.query(cls).filter_by(name=name).first()

    def get_articles(self):
        return self.articles
