import sys, os, pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../lib")))

from db import Base, engine, SessionLocal
from models import Author, Article, Magazine

@pytest.fixture(autouse=True)
def setup_db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

def test_author_initialization():
    a = Author(name="Grace Wambui")
    assert a.name == "Grace Wambui"

def test_author_save_and_find():
    session = SessionLocal()
    saved = Author.save(session, "David Ochieng")
    assert saved.id is not None

    by_id = Author.find_by_id(session, saved.id)
    by_name = Author.find_by_name(session, "David Ochieng")

    assert by_id.name == "David Ochieng"
    assert by_name.id == saved.id
    session.close()

def test_author_name_validation():
    with pytest.raises(ValueError):
        Author(name="   ")

def test_author_articles_relationship():
    session = SessionLocal()
    author = Author.save(session, "Mercy Atieno")
    mag = Magazine.save(session, "Eco Kenya", "Environment")
    Article.save(session, "Green Nairobi", author.id, mag.id)

    fetched = Author.find_by_id(session, author.id)
    articles = fetched.get_articles()

    assert len(articles) == 1
    assert articles[0].title == "Green Nairobi"
    session.close()
