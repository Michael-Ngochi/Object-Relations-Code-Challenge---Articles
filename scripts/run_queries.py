# scripts/run_queries.py

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../lib")))

from db import SessionLocal
from models import Author, Magazine, Article

def run():
    session = SessionLocal()

    # --- Create and insert data ---
    author = Author(name="John Doe")
    magazine = Magazine(name="Science Today", category="Science")
    session.add_all([author, magazine])
    session.commit()

    article = Article(title="Quantum Breakthrough", author_id=author.id, magazine_id=magazine.id)
    session.add(article)
    session.commit()

    # --- Query data ---
    articles = session.query(Article).all()
    for art in articles:
        print(f"{art.title} | Author ID: {art.author_id} | Magazine ID: {art.magazine_id}")

    session.close()

if __name__ == "__main__":
    run()
