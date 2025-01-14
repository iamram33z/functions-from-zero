# Import Wikipedia
import wikipedia


# Returns the summary of the search query
def search(query, length=4):
    return wikipedia.summary(query, sentences=length)

print(search("Python programming"))