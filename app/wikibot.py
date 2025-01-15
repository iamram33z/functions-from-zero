# Integrate Click, Wikipedia
import click
from mylib.bot import search


@click.command()
@click.option(
    "--query",
    prompt="Wikipedia Query to search",
    help="The query we want to search in Wikipedia.",
)
@click.option(
    "--length",
    default=4,
    help="The number of sentences to return in the search result.",
)

# Returns the summary of the search query
def searcher(query="Bill Gates", length=5):
    result = search(query, length=length)
    click.echo(click.style(f"{result}", fg="red"))


if __name__ == "__main__":
    searcher()
