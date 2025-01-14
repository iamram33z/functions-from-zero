import wikipedia # type: ignore

# Returns the summary of the search query
def search(query="Microsoft", length=4):
    result = wikipedia.summary(query, sentences=length)
    return result