# coding: utf8
""" Test cases """

from urduhack.urdu_characters import URDU_ALPHABETS

from stop_words import STOP_WORDS


def test_stop_words():
    """ Test case"""
    for word in STOP_WORDS:
        for character in word:
            assert character in URDU_ALPHABETS
