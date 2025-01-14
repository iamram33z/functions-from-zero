# Create the Test File for the WikiBot Class
from wikibot import search

def test_search():
    assert "Python" in search("Python programming")

