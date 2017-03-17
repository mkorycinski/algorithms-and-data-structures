import unittest


def binary_search(arr, ele):

    first = 0
    last = len(arr) - 1

    found = False

    while first <= last and not found:

        mid = (first + last) // 2

        if arr[mid] == ele:
            found = True

        else:
            if ele < arr[mid]:
                last = mid - 1
            else:
                first = mid + 1

    return found


def binary_search_rec(arr, ele):
    if len(arr) == 0:
        return False

    else:
        mid = len(arr) // 2

        if arr[mid] == ele:
            return True

        else:
            if ele < arr[mid]:
                return binary_search_rec(arr[:mid], ele)
            else:
                return binary_search_rec(arr[mid+1:], ele)


class TestSearches(unittest.TestCase):

    def setUp(self):
        self.arr = [1,2,3,4,5,6,7,8,9,10]

    def test_binary_search(self):
        self.assertFalse(binary_search(self.arr, 25))
        self.assertTrue(binary_search(self.arr, 5))

    def test_binary_search_rec(self):
        self.assertFalse(binary_search_rec(self.arr, 25))
        self.assertTrue(binary_search_rec(self.arr, 5))

if __name__ == '__main__':
    unittest.main()