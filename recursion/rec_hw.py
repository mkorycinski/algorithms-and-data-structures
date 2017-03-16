import unittest


def rec_sum(n):

    if n == 0:
        return 0

    else:
        return n + rec_sum(n-1)


def sum_func(n):

    if n <= 9:
        return n

    else:
        return n % 10 + sum_func(int(n/10))


def word_split(sentence, arr, output=None):

    if not output:
        output = []

    for word in arr:
        if sentence.startswith(word):
            output.append(word)

            return word_split(sentence[len(word):], arr, output)

    return output


class TestHomeWork(unittest.TestCase):

    def test_rec_sum(self):
        self.assertEqual(rec_sum(4), 10)
        self.assertEqual(rec_sum(5), 15)
        self.assertEqual(rec_sum(6), 21)
        self.assertEqual(rec_sum(1), 1)
        self.assertEqual(rec_sum(0), 0)

    def test_sum_func(self):
        self.assertEqual(sum_func(4321), 10)
        self.assertEqual(sum_func(54321), 15)
        self.assertEqual(sum_func(654321), 21)
        self.assertEqual(sum_func(1), 1)
        self.assertEqual(sum_func(0), 0)

    def test_word_split(self):
        self.assertListEqual(word_split('themanran', ['the', 'ran', 'man']),
                             ['the', 'man', 'ran'])
        self.assertListEqual(word_split('ilovedogsJohn',
                                        ['i', 'am', 'a', 'dogs', 'lover',
                                         'love', 'John']),
                             ['i', 'love', 'dogs', 'John'])
        self.assertListEqual(word_split('themanran', ['clown', 'ran', 'man']),
                             [])

if __name__ == '__main__':
    unittest.main()
