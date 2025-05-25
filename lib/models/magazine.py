from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, validates
from db import Base
from models.article import Article  # to link relationships

class Magazine(Base):
    __tablename__ = "magazines"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique=True)
    category = Column(String(255), nullable=False)


    articles = relationship("Article", back_populates="magazine", cascade="all, delete")

    def __init__(self, name, category):
        self.name = name
        self.category = category

    def __repr__(self):
        return f"<Magazine(id={self.id}, name='{self.name}', category='{self.category}')>"


    @validates("name")
    def validate_name(self, key, value):
        if not value or not value.strip():
            raise ValueError("Magazine name cannot be empty.")
        return value.strip()

    @validates("category")
    def validate_category(self, key, value):
        if not value or not value.strip():
            raise ValueError("Magazine category cannot be empty.")
        return value.strip()

    # --- SQL Methods ---
    @classmethod
    def save(cls, session, name, category):
        magazine = cls(name=name, category=category)
        session.add(magazine)
        session.commit()
        return magazine

    @classmethod
    def find_by_id(cls, session, magazine_id):
        return session.query(cls).filter_by(id=magazine_id).first()

    @classmethod
    def find_by_name(cls, session, name):
        return session.query(cls).filter_by(name=name).first()

    @classmethod
    def find_by_category(cls, session, category):
        return session.query(cls).filter_by(category=category).all()

    def get_articles(self):
        return self.articles
