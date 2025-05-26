import sys, os, pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../lib")))

from db import Base, engine, SessionLocal
from models import Article, Author, Magazine

@pytest.fixture(autouse=True)
def setup_db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

def test_article_initialization():
    a = Article(title="Urban Farming", author_id=1, magazine_id=1)
    assert a.title == "Urban Farming"

def test_article_save_and_find():
    session = SessionLocal()
    author = Author.save(session, "Lilian Wangechi")
    mag = Magazine.save(session, "Agri Life", "Farming")

    article = Article.save(session, "Organic Farming in Kenya", author.id, mag.id)

    by_id = Article.find_by_id(session, article.id)
    by_title = Article.find_by_title(session, "Organic Farming in Kenya")
    by_author = Article.find_by_author(session, author.id)
    by_mag = Article.find_by_magazine(session, mag.id)

    assert by_id.title == "Organic Farming in Kenya"
    assert by_title.id == article.id
    assert len(by_author) == 1
    assert len(by_mag) == 1
    session.close()

def test_article_title_validation():
    with pytest.raises(ValueError):
        Article(title=" ", author_id=1, magazine_id=1)

def test_article_relationships():
    session = SessionLocal()
    author = Author.save(session, "James Mwaura")
    mag = Magazine.save(session, "Clean Energy KE", "Environment")
    article = Article.save(session, "Solar Trends 2025", author.id, mag.id)

    assert article.get_author().name == "James Mwaura"
    assert article.get_magazine().name == "Clean Energy KE"
    session.close()
