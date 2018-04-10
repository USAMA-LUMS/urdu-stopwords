"""
Generate json and text file format for Urdu stopwords
"""

import os
import sys
import json
import codecs

sys.path.append(os.path.join(os.path.dirname(__file__)))
from stop_words import STOP_WORDS


def generate_data_files():
    """
    Generate Urdu stop words data text and json file
    """
    data = list(STOP_WORDS)

    with codecs.open('urdu_stopwords.json', 'w', encoding="utf-8") as outfile:
        json.dump(data, outfile, ensure_ascii=False)

    with codecs.open('urdu_stopwords.txt', 'w', encoding="utf-8") as f:
        for word in data:
            f.write(word + "\n")


if __name__ == "__main__":
    generate_data_files()
