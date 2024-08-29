
FILEPATH = 'books/frankenstein.txt'


def main():
    report = generate_report(FILEPATH)
    print(f'{report}')


def get_file_text(filepath: str) -> str:
    """ Gets the file text
    Returns a string with all the content
    """
    with open(filepath, 'r', encoding='UTF-8') as book:
        content = book.read()
        return content


# ------------------------------ CONTENT RELATED ----------------------------- #

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
    return obj['value']


def generate_report(filepath: str) -> str:
    """ Generates a report:
        - The book file path
        - Count of total words within the document
        - Details about letters in text sorted by the highest occurrence
        Returns str
    """
    report = ''
    content = get_file_text(FILEPATH)

    # Gets various info about the text
    words_count = count_words(content)
    characters = count_characters(content)
    found_words = find_words_occurrences(['monster', 'love'], content)

    # [ Report ] Adds lines for file and words count
    report += f'--- Begin report of {filepath} ---\n'
    report += f'{words_count} words found in the document\n\n'

    # Organize found character by their occurrence value
    # - re-organize obj structure for sorting step
    characters_list = []
    for char in characters:
        characters_list.append({
            "name": char,
            "value": characters[char]
        })

    # - sorting - highest on top, lowest at the bottom
    characters_list.sort(reverse=True, key=sort_on)

    # [ REPORT ] Adds lines for characters info to read
    for character_details in characters_list:
        char = character_details['name']
        if char.isalpha():
            value = character_details['value']
            report += f"\nThe '{char}' character was found {value} times"

    return report


main()
