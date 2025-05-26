import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "lib")))

from db import SessionLocal
from models import Author, Magazine, Article

def create_author(session):
    name = input("Enter author name: ").strip()
    try:
        author = Author.save(session, name)
        print(f"Author saved with ID {author.id}")
    except Exception as e:
        print(f"Error: {e}")

def create_magazine(session):
    name = input("Enter magazine name: ").strip()
    category = input("Enter magazine category: ").strip()
    try:
        magazine = Magazine.save(session, name, category)
        print(f"Magazine saved with ID {magazine.id}")
    except Exception as e:
        print(f" Error: {e}")

def create_article(session):
    title = input("Enter article title: ").strip()
    try:
        author_id = int(input("Enter author ID: "))
        magazine_id = int(input("Enter magazine ID: "))
        article = Article.save(session, title, author_id, magazine_id)
        print(f"Article saved with ID {article.id}")
    except Exception as e:
        print(f"Error: {e}")

def list_authors(session):
    authors = session.query(Author).all()
    for a in authors:
        print(f"[{a.id}] {a.name}")

def list_magazines(session):
    magazines = session.query(Magazine).all()
    for m in magazines:
        print(f"[{m.id}] {m.name} - {m.category}")

def list_articles(session):
    articles = session.query(Article).all()
    for a in articles:
        print(f"[{a.id}] {a.title} (Author ID: {a.author_id}, Magazine ID: {a.magazine_id})")

def main():
    session = SessionLocal()
    while True:
        print("\n MAIN MENU")
        print("1. Create Author")
        print("2. Create Magazine")
        print("3. Create Article")
        print("4. View Authors")
        print("5. View Magazines")
        print("6. View Articles")
        print("0. Exit")

        choice = input("Select an option: ").strip()
        if choice == "1":
            create_author(session)
        elif choice == "2":
            create_magazine(session)
        elif choice == "3":
            create_article(session)
        elif choice == "4":
            list_authors(session)
        elif choice == "5":
            list_magazines(session)
        elif choice == "6":
            list_articles(session)
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")
    session.close()

if __name__ == "__main__":
    main()
