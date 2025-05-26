import sys, os, pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../lib")))

from db import Base, engine, SessionLocal
from models import Magazine, Author, Article

@pytest.fixture(autouse=True)
def setup_db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

def test_magazine_initialization():
    m = Magazine(name="Health Plus", category="Health")
    assert m.name == "Health Plus"
    assert m.category == "Health"

def test_magazine_save_and_find():
    session = SessionLocal()
    saved = Magazine.save(session, "Safari Digest", "Travel")

    by_id = Magazine.find_by_id(session, saved.id)
    by_name = Magazine.find_by_name(session, "Safari Digest")
    by_category = Magazine.find_by_category(session, "Travel")

    assert by_id.name == "Safari Digest"
    assert by_name.id == saved.id
    assert len(by_category) == 1
    session.close()

def test_magazine_name_category_validation():
    with pytest.raises(ValueError):
        Magazine(name="", category="Health")

    with pytest.raises(ValueError):
        Magazine(name="Tech", category=" ")

def test_magazine_articles_relationship():
    session = SessionLocal()
    mag = Magazine.save(session, "Innovation KE", "Tech")
    author = Author.save(session, "Kevin Ndungu")
    Article.save(session, "Kenya's Tech Boom", author.id, mag.id)

    fetched = Magazine.find_by_id(session, mag.id)
    articles = fetched.get_articles()

    assert len(articles) == 1
    assert articles[0].title == "Kenya's Tech Boom"
    session.close()
