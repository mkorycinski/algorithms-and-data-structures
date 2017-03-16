import unittest


def rec_coin(target, coins):

    if target == 0 or target == coins[-1]:
        return target

    else:
        n = int(target / coins[-1])

        return n + rec_coin(target - (n * coins[-1]), coins[:-1])


class TestCoins(unittest.TestCase):
    def test_check(self):
        coins = [1, 5, 10, 25]
        self.assertEqual(rec_coin(45, coins), 3)
        self.assertEqual(rec_coin(23, coins), 5)
        self.assertEqual(rec_coin(74, coins), 8)


if __name__ == '__main__':
    unittest.main()
