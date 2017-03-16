import unittest


def sentence_rev(s):
    words = []
    length = len(s)
    spaces = [' ']
    i = length - 1

    while i >= 0:

        if s[i] not in spaces:

            word_end = i

            while i >= 0 and s[i] not in spaces:
                i -= 1

            words.append(s[i+1:word_end+1])

        i -= 1

    return ' '.join(words)


def sentence_rev3(s):
    words = []
    length = len(s)
    spaces = [' ']
    i = 0

    while i < length:

        if s[i] not in spaces:

            word_start = i

            while i < length and s[i] not in spaces:
                i += 1

            words.append(s[word_start:i])

        i += 1

    return ' '.join(reversed(words))


def sentence_rev2(sentence):
    sentence = sentence.strip().split()

    i = len(sentence) - 1
    rev_sentence = ''
    while i >= 0:
        rev_sentence += sentence[i]

        if i != 0:
            rev_sentence += ' '
        i -= 1

    return rev_sentence


def sentence_rev1(sentence):
    return ' '.join(sentence.strip().split()[::-1])


class TestRev(unittest.TestCase):
    def test_sentence_rev(self):
        self.assertEqual(sentence_rev('     space before'),
                         'before space')
        self.assertEqual(sentence_rev('space after    '),
                         'after space')
        self.assertEqual(sentence_rev('   Hello John    how are you    '),
                         'you are how John Hello')
        self.assertEqual(sentence_rev('1'),
                         '1')