"""Checks if anagrams"""

import unittest



# It's not optimal
def anagram2(s1, s2):
    s1 = s1.replace(' ','')
    s2 = s2.replace(' ', '')

    return sorted(s1) == sorted(s2)

# moja metoda okazala sie dobra :D
def anagram(word1, word2):
    db = {}
    # Tutaj mialem strip i split zeby usunac wszystkie biale znaki
    # a nie tylko spacje, w sumie spacje stykna.
    word1 = word1.replace(' ', '').lower()
    word2 = word2.replace(' ', '').lower()

    # Tego nie mialem, przydaje sie!
    if len(word1) != len(word2):
        return False

    for letter in word1:
        if letter not in db:
            db[letter] = 0
        db[letter] += 1

    for letter in word2:
        try:
            db[letter] -= 1
        except KeyError:
            return False

    for v in db.values():
        if v != 0:
            return False

    return True


class AnagramTest(unittest.TestCase):
    def test_anagram(self):
        self.assertEqual(anagram('go go go', 'gggooo'), True)
        self.assertEqual(anagram('abc', 'cba'), True)
        self.assertEqual(anagram('Hi man', 'hi     man'), True)
        self.assertEqual(anagram('aabbcc', 'aabbc'), False)
        self.assertEqual(anagram('123', '1 2'), False)

if __name__ == '__main__':
    unittest.main()