import task1

text = input('Enter text: ')
print('Amount of sentences: ' + str(task1.amount_of_sentences(text)))
print('Amount of non-declarative sentences: ' + str(task1.amount_of_non_declarative_sentences(text)))
print('Average sentence length: ' + str(task1.average_sentence_lenght(text)))
print('Average word length: ' + str(task1.average_word_lenght(text)))


