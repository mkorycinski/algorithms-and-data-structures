import unittest

def solution(s):

    r = ''
    l = len(s)

    if l == 0:
        return ''

    if l == 1:
        return s+'1'

    last = s[0]
    cnt = 1

    i = 1

    while i < l:
        if s[i] == s[i-1]:
            cnt += 1
        else:
            r = r + s[i-1] + str(cnt)
            cnt = 1

        i += 1

    r = r + s[i-1] + str(cnt)

    return r

def solution1(s):

    if len(s) == 0:
        return ''

    curr_char = s[0]
    curr_count = 1
    compressed = ''

    for char in s[1:]:
        if char == curr_char:
            curr_count += 1
        else:
            if curr_count <= 1:
                compressed += curr_char
            else:
                compressed += '%s%d' % (curr_char, curr_count)

            curr_char = char
            curr_count = 1

    compressed += '%s%d' % (curr_char, curr_count)
    return compressed


class TestSolution(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(solution(''),'')
        self.assertEqual(solution('AABBCC'),'A2B2C2')
        self.assertEqual(solution('AAABCCDDDDD'), 'A3B1C2D5')