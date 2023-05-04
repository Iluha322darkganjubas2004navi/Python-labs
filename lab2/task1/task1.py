import re
from constants import (WORDS, NUMBERS, SENTENCES, NON_DECL_SENTENCES,
                  ABBREVIATIONS1, ABBREVIATIONS2)

def amount_of_sentences(text: str) -> int:
    text = text.lower()
    amount = len(re.findall(SENTENCES, text))

    for abbreviation in ABBREVIATIONS1:
        amount -= text.count(abbreviation)

    for abbreviation in ABBREVIATIONS2:
        amount -= text.count(abbreviation) * 2

    return

def amount_of_non_declarative_sentences(text: str) -> int:
    return len(re.findall(NON_DECL_SENTENCES, text))