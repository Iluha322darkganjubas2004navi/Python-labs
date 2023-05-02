import re
from constants import (WORDS, NUMBERS, SENTENCES, NON_DECL_SENTENCES,
                  ABBREVIATIONS1, ABBREVIATIONS2)

def amount_of_sentences(text: str)->int:
    text=text.lower()
    amount = len(re.findall(SENTENCES, text))
