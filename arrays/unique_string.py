import unittest


def uni_char(s):
    return len(set(s)) == len(s)


def solution(s):
    seen = []

    for i in s:
        if i in seen:
            return False

        seen.append(i)

    return True

class TestSolution(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(solution('aabcd'), False)
        self.assertEqual(solution('abcde'), True)