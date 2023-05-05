import task1

text = input('Enter the text:\n')

sentences = task1.sentences_split(text)
sentences_amount = task1.sentences_amount(sentences)
non_declarative_sentences_amount = task1.non_declarative_sentences_amount(sentences)
average_sentences_length = task1.average_sentence_length(sentences)
average_word_length = task1.average_word_length(text)
k=10
n=4
n_grams = task1.top_n_grams(k, n, sentences)

print('Amount of sentences: ', sentences_amount)
print('Amount of non-declarative sentences: ', non_declarative_sentences_amount)
print('Average length of the sentence in characters: ', average_sentences_length)
print('Average length of the word in the text in characters', average_word_length)

if n_grams == {}:
    print('No grams found.')
else:
    print('Top K-repeated N-grams: ')
    for gram, count in n_grams.items():
        print(gram)