import task1


def test_sentences_split_1():
    res = task1.sentences_split('Heh! Babijon?')
    assert len(res) == 2
    assert res == ['Heh!', 'Babijon?']


def test_sentences_split_2():
    res = task1.sentences_split('Test?.. "Test, test, test!" Test...')
    assert len(res) == 3
    assert res == ['Test?..', '"Test, test, test!"', 'Test...']


def test_sentences_split_3():
    res = task1.sentences_split('E. G. Brendon. Dr. Bro! Mr.Fento, \'test!..\'')
    assert len(res) == 3
    assert res == ['E. G. Brendon.', 'Dr. Bro!', 'Mr. Fento, \'test!..\'']


def test_sentences_amount_1():
    sent = task1.sentences_split('Mr.Mia! How are you?.. I\'m fine!')
    res = task1.sentences_amount(sent)
    assert res == 3


def test_non_declarative_sentences_amount_1():
    sent = task1.sentences_split('Test!.. Test... Test. Test?.. Test! Test test test.')
    res = task1.non_declarative_sentences_amount(sent)
    assert res == 3


def test_average_sentence_length_1():
    sent = task1.sentences_split('Test!.. Test... Test Test?.. Test test test.')
    res = task1.average_sentence_length(sent)
    assert res == 7


def test_average_word_length_1():
    res = task1.average_word_length('Test test. testing')
    assert res == 5


def test_top_n_grams_1():
    sent = task1.sentences_split('Ment tot. Ment tot ment tot ment bra bru bra tot bra bru. Bru bra bru!..')
    res = task1.top_n_grams(5, 2, sent)
    assert res == {"('ment', 'tot')": 3, "('bra', 'bru')": 3, "('tot', 'ment')": 2, "('bru', 'bra')": 2, "('ment', 'bra')": 1}