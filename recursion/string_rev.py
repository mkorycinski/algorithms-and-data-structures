import unittest


def solution(s):
    if not s:
        return ''

    return s[-1] + solution(s[:-1])


class TestReverse(unittest.TestCase):
    def test_rev(self):
        self.assertEqual(solution('hello'), 'olleh')
        self.assertEqual(solution('hello world'), 'dlrow olleh')
        self.assertEqual(solution('123456789'), '987654321')


if __name__ == '__main__':
    unittest.main()
    # print(solution('hello'))