from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, validates
from db import Base

class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    author_id = Column(Integer, ForeignKey("authors.id"))
    magazine_id = Column(Integer, ForeignKey("magazines.id"))


    author = relationship("Author", back_populates="articles")
    magazine = relationship("Magazine", back_populates="articles")

    def __init__(self, title, author_id, magazine_id):
        self.title = title
        self.author_id = author_id
        self.magazine_id = magazine_id

    def __repr__(self):
        return f"<Article(id={self.id}, title='{self.title}')>"

    @validates("title")
    def validate_title(self, key, value):
        if not value or not value.strip():
            raise ValueError("Article title cannot be empty.")
        return value.strip()

    # --- SQL Methods ---
    @classmethod
    def save(cls, session, title, author_id, magazine_id):
        article = cls(title=title, author_id=author_id, magazine_id=magazine_id)
        session.add(article)
        session.commit()
        return article

    @classmethod
    def find_by_id(cls, session, article_id):
        return session.query(cls).filter_by(id=article_id).first()

    @classmethod
    def find_by_title(cls, session, title):
        return session.query(cls).filter_by(title=title).first()

    @classmethod
    def find_by_author(cls, session, author_id):
        return session.query(cls).filter_by(author_id=author_id).all()

    @classmethod
    def find_by_magazine(cls, session, magazine_id):
        return session.query(cls).filter_by(magazine_id=magazine_id).all()

    def get_author(self):
        return self.author

    def get_magazine(self):
        return self.magazine
