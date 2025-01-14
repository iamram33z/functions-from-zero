# Create the Test File for the WikiBot Class
from wikibot import searcher
from mylib.bot import search
from click.testing import CliRunner

def  test_search ():
    assert "Python" in search("Python programming")

def test_searcher ():
    runner = CliRunner()
    result = runner.invoke(searcher, ['--query', 'Python programming'])
    assert "Python" in result.output