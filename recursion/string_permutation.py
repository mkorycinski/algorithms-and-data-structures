import unittest


def permute(s):
    out = []

    if len(s) == 1:
        return [s]

    for i, let in enumerate(s):

        for perm in permute(s[:i] + s[i+1:]):

            out.append(let+perm)

    return out


class TestPerm(unittest.TestCase):
    def test(self):
        self.assertListEqual(permute('abc'),
                     ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
        self.assertListEqual(permute('dog'),
                            ['dog', 'dgo', 'odg', 'ogd', 'gdo', 'god'])


if __name__ == '__main__':
    print(permute('ab'))
