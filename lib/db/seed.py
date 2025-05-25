import sys
import os

# Add lib/ to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../lib")))

from db import SessionLocal
from models import Author, Magazine, Article

session = SessionLocal()

# --- Authors ---
authors = [
    Author(name="Wanjiru Kamau"),
    Author(name="Mwangi Njoroge"),
    Author(name="Achieng Otieno"),
    Author(name="Ali Yusuf"),
    Author(name="Nyambura Kilonzo"),
]

# --- Magazines ---
magazines = [
    Magazine(name="Tech254", category="Technology"),
    Magazine(name="Afya Leo", category="Health"),
    Magazine(name="Shujaa Weekly", category="History"),
    Magazine(name="BizKenya", category="Business"),
    Magazine(name="Lifestyle KE", category="Lifestyle"),
]

session.add_all(authors + magazines)
session.commit()

# --- Articles ---
articles = [
    Article(title="The Rise of Mobile Money", author_id=authors[0].id, magazine_id=magazines[0].id),
    Article(title="Nutrition and Affordable Eating", author_id=authors[1].id, magazine_id=magazines[1].id),
    Article(title="Unsung Heroes of the Mau Mau", author_id=authors[2].id, magazine_id=magazines[2].id),
    Article(title="How SMEs are Powering Kenya’s Economy", author_id=authors[3].id, magazine_id=magazines[3].id),
    Article(title="Nairobi's Evolving Fashion Scene", author_id=authors[4].id, magazine_id=magazines[4].id),
    Article(title="Digital Agriculture Tools in Kenya", author_id=authors[0].id, magazine_id=magazines[0].id),
    Article(title="Mental Health Awareness in Schools", author_id=authors[2].id, magazine_id=magazines[1].id),
]

session.add_all(articles)
session.commit()

session.close()
print("database seeded.")
