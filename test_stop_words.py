# coding: utf8
""" Test cases updated"""

from urduhack.normalization.character import COMBINE_URDU_CHARACTERS
from urduhack.urdu_characters import URDU_ALPHABETS

from stop_words import STOP_WORDS


def test_stop_words():
    """ Test case"""
    for word in STOP_WORDS:
        for chars in COMBINE_URDU_CHARACTERS:
            assert len(chars) == 2
            assert chars not in word

        for character in word:
            assert character in URDU_ALPHABETS, F"Incorrect word: {word} and char: {character}"


def test_stop_words_txt_file():
    """ Test case"""

    stop_words_file_list = [line.strip() for line in open("stop_words.txt", encoding="utf8")]
    for word in STOP_WORDS:
        assert word in stop_words_file_list, F"Word: {word} not found in stop_words.txt file!"


def chunk_it(seq, num):
    """
    Converted list into multiple sub list
    Args:
        seq: list
        num: integer
    Returns:
        list
    """
    avg = len(seq) / float(num)
    out = []
    last = 0.0

    while last < len(seq):
        out.append(seq[int(last):int(last + avg)])
        last += avg

    return out


def sorted_stopwords(words):
    """Sort the stop words"""
    print(f"Stop words Count: {len(words)}")
    stop_words = sorted(words)
    lists = chunk_it(stop_words, 26)

    for word_list in lists:
        string_print = ""
        for line in word_list:
            string_print = string_print + " " + line.strip()

        print(string_print)
        string_print = ""


def set_to_txt(words):
    """
    Convert stop words set into the text file
    """
    stop_words = sorted(words)
    with open('stop_words.txt', 'w', encoding="utf8") as file:
        for item in stop_words:
            file.write("%s\n" % item)
