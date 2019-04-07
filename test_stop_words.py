# coding: utf8
""" Test cases """

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
    lists = chunk_it(stop_words, 16)

    for word_list in lists:
        string_print = ""
        for line in word_list:
            string_print = string_print + " " + line.strip()

        print(string_print)
        string_print = ""
