

def count_words(content: str) -> int:
    """ Count words in text
    Returns total count of words
    """
    return len(content.split())


def count_characters(content: str) -> dict:
    """ Counts characters and store the details of each
       Returns a dictionary { "name": str, "value": int }
    """
    characters = {}
    for char in content:
        char = char.lower()
        if char == '':
            char = '_space_'
        if char not in characters:
            characters[char] = 0
        characters[char] += 1

    return characters


def find_words_occurrences(words: list, content: str) -> dict | None:
    """ Find words occurrences in the text """
    requested_words = {}
    for word in words:
        if word not in requested_words:
            requested_words[word] = 0

    content_words = content.split()
    for content_word in content_words:
        if content_word in requested_words:
            requested_words[content_word] += 1
    return requested_words if len(requested_words) else None


def sort_on(obj):
    """ Returns an object value """
    return obj[1]

