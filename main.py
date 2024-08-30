import sys

FILEPATH = 'books/frankenstein.txt'
IS_DEFAULT_RUN = True

################################################################################
#
# A script to read text files ( .txt ) and provide insights about it
# Technically reading the file and parsing it to generates info
#
# Base
# - total words count
# - details about occurrence of alphabetical letter used
#
# Extra - dynamical implementation
# - Arguments handling on command execution
# - Prompt inputs entries from user
#
################################################################################


def main():
    try:
        should_prompt = handle_arguments_customization()
        if should_prompt:
            words = prompt_user()
            report = generate_report(FILEPATH, words)
            print(f'{report}')
    except KeyboardInterrupt:
        print('\nExecution interrupted. Ending Program.')
        sys.exit(0)
    except Exception as e:
        print('❌ Error occurred', e)
        sys.exit(0)


def get_file_text(filepath: str) -> str:
    """ Gets the file text
    Returns a string with all the content
    """
    with open(filepath, 'r', encoding='UTF-8') as book:
        content = book.read()
        return content


# -------------------------------- USER INPUT -------------------------------- #
################################################################################
#
# This script can prompt the user to execute the process with users' input
# This also has a default behaviour - reading filepath from a static dev file
# --> books/frankenstein.txt
#
# - asking for the filepath
# - asking for words words to search for ( separated by a comma )
# Execution example: "python main.py will prompt
#
################################################################################
def prompt_user() -> list:
    """ Prompt User for
    - a filepath
    - any words to found in the text
    """
    custom_check_message = "Would you like to run in it by default ?:"
    filepath_message = "Text* file path to read:"
    words_txt_message = "Any word(s) you'd like to search in the txt \
                   \n( enter to skip or provide words or terms separated by a comma ):"

    # Formatting and prompt input
    space = ' '
    IS_DEFAULT_RUN = False \
        if input('▶️' + space + custom_check_message + space) \
        else True
    if IS_DEFAULT_RUN:
        print(f'\t> Running by default.\n')

    # Gets decision about running it as custom or default
    words = []
    if not IS_DEFAULT_RUN:
        filepath = input('▶️' + space + filepath_message + space)
        words_to_find = input('▶️' + space + words_txt_message + space)
        if filepath:
            FILEPATH = filepath

        if words_to_find:
            words = [x.strip() for x in words_to_find.split(',')]

    return words


# ---------------------------- ARGUMENTS HANDLING ---------------------------- #
################################################################################
#
# This script can accepts 2 arguments
# - filepath
# - words to search for ( separated by a comma )
# Execution example: "python main.py <filepath> <words>
# Execution example: "python main.py books/mytext.txt love, morning, search
# Returns a boolean:
# - True if the process did not go through this function
# - False if the process did go through the function
#
################################################################################
def handle_arguments_customization() -> bool:
    """ [ CLI ] handles arguments passed through CLI """
    should_prompt = True
    if len(sys.argv) > 1:
        args = sys.argv
        filename = args[1]
        words = [word.strip(',') for word in args[2:]]
        should_prompt = False
        if ".txt" not in filename:
            print('Only text files can be red. You may try again.')
            return
        FILEPATH = filename
        report = generate_report(FILEPATH, words)
        print(report)
    return should_prompt

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
    return obj[1]


def generate_report(filepath: str, searched_words: list) -> str:
    """ Generates a printable report:
            - The book file path
            - Count of total words within the document
            - Details about letters in text sorted by the highest occurrence
    Returns str
    """
    report = '\n\n'
    content = get_file_text(filepath)

    # [ Report ] Adds lines for file and words count
    report += f'--------- Begin report of {filepath} --------- \n\n'

    # [ Report ] Adds lines for file and words count
    words_count = count_words(content)
    report += f'\n\t ▶️ {words_count} words found in the document.'

    # [ Report ] Adds lines for Searched words
    if len(searched_words):
        found_words = find_words_occurrences(searched_words, content)

        if len(found_words):
            report += '\n\n\n'
            report += '\t------------------------------------------\n'
            report += '\t------------ Researched words ------------\n'
            report += '\t------------------------------------------\n'
            # Ordering by number of occurrence
            found_words_list = [*found_words.items()]
            found_words_list.sort(reverse=True, key=sort_on)
            for found_word in found_words_list:
                report += \
                    f'\n\t{found_word[1]} mentions of "{found_word[0]}"'

    # [ REPORT ] Adds lines for characters info to read
    if len(searched_words):
        report += '\n\n'
    report += '\n\n'
    report += '\t------------------------------------------\n'
    report += '\t----------- Letters occurrence -----------\n'
    report += '\t------------------------------------------\n'

    # - sorting - highest on top, lowest at the bottom
    characters = count_characters(content)
    characters_list = [*characters.items()]
    characters_list.sort(reverse=True, key=sort_on)

    for character_details in characters_list:
        char = character_details[0]
        if char.isalpha():
            value = character_details[1]
            report += f"\n\tThe '{char}' character was found {value} times"
    report += '\n\n'
    return report


main()
