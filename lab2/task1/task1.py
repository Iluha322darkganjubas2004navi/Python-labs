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

    return amount


def amount_of_non_declarative_sentences(text: str) -> int:
    return len(re.findall(NON_DECL_SENTENCES, text))


def average_sentence_lenght(text: str) -> float:
    nums = re.findall(NUMBERS, text)
    words = [word for word in re.findall(WORDS, text) if word not in nums]
    words_len = sum(len(word) for word in words)

    if amount_of_sentences(text) != 0:
        return round(words_len / amount_of_sentences(text), 2)
    else:
        return 0