import unittest
from structures import Stack


def balance_check(case):

    openings = set('{([')
    closings = {'(': ')', '{':'}', '[':']'}

    if len(case) % 2 != 0:
        return False

    if case[0] in closings:
        return False

    if case[-1] in openings:
        return False

    brackets = Stack()

    for elem in case:
        if elem in openings:
            brackets.push(elem)
        else:
            if elem != closings[brackets.pop()]:
                return False

    return len(brackets) == 0


class TestBalanceCheck(unittest.TestCase):

    def test_balance(self):
        self.assertEqual(balance_check('[]'), True)
        self.assertEqual(balance_check('[{](})'), False)
        self.assertEqual(balance_check('{()[]}'), True)
        self.assertEqual(balance_check('()()({)}'), False)


if __name__ == '__main__':
    unittest.main()