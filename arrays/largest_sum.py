import unittest


def lsum(arr):

    if len(arr) == 0:
        return 0

    max_sum = current_sum = arr[0]

    for num in arr[1:]:
        current_sum = max(current_sum+num, num)
        max_sum = max(current_sum, max_sum)

    return max_sum

# Doesn't work
def lsum_old(arr):
    max_sum = 0
    tmp_sum = 0
    # start = 0
    # end = 0

    if len(arr) == 0:
        return 0

    for elem in arr:
        if tmp_sum + elem > 0:
            tmp_sum += elem
        else:
            max_sum = tmp_sum
            tmp_sum = 0

    if max_sum < tmp_sum:
        max_sum = tmp_sum

    return max_sum


class LargeContTest(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(lsum([1,2,-1,3,4,-1]), 9)
        self.assertEqual(lsum([1, 2, -1, 3,4,10,10,-10,-1]), 29)
        self.assertEqual(lsum([-1, 1]), 1)

if __name__ == '__main__':
    unittest.main()