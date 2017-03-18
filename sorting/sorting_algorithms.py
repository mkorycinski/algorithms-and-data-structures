import unittest


def bubble_sort(arr):
    for n in range(len(arr)-1, 0, -1):
        for k in range(n):
            if arr[k] > arr[k+1]:
                temp = arr[k]
                arr[k] = arr[k+1]
                arr[k+1] = temp


def selection_sort(arr):
    for fillslot in range(len(arr)-1, 0, -1):

        max_pos = 0

        for loc in range(1, fillslot+1):

            if arr[loc] > arr[max_pos]:
                max_pos = loc

        temp = arr[fillslot]
        arr[fillslot] = arr[max_pos]
        arr[max_pos] = temp


def merge_sort(arr):
    if len(arr) > 1:

        mid = len(arr) // 2

        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):

            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1

            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


def insert_sort(arr):
    for i in range(1, len(arr)):
        curr_val = arr[i]
        position = i

        while position > 0 and arr[position-1] > curr_val:

            arr[position] = arr[position - 1]
            position -= 1

        arr[position] = curr_val


def shell_sort(arr):
    sublist_count = len(arr) // 2

    while sublist_count > 0:
        for start in range(sublist_count):

            gap_insertion_sort(arr, start, sublist_count)

        sublist_count //= 2


def gap_insertion_sort(arr, start, gap):
    for i in range(start + gap, len(arr), gap):
        curr_val = arr[i]
        position = i

        while position >= gap and arr[position-gap] > curr_val:

            arr[position] = arr[position-gap]
            position -= gap
        arr[position] = curr_val


# def quick_sort(arr):
#     quick_sort_help(arr, 0, len(arr)-1)
#
#
# def quick_sort_help(arr, first, last):
#     if first < last:
#
#         split_point = partition(arr, first, last)
#
#         quick_sort_help(arr, first, split_point-1)
#         quick_sort_help(arr, split_point+1, last)
#
#
# def partition(arr, first, last):
#
#     pivot = first
#
#     left_mark = first + 1
#     right_mark = last
#
#     done = False
#
#     while not done:
#         while left_mark <= right_mark and arr[left_mark] <= pivot:
#             left_mark += 1
#
#         while arr[right_mark] >= pivot and right_mark >= left_mark:
#             right_mark -= 1
#
#         if right_mark < left_mark:
#             done = True
#
#         else:
#             temp = arr[left_mark]
#             arr[left_mark] = arr[right_mark]
#             arr[right_mark] = temp
#
#     temp = arr[first]
#     arr[first] = arr[right_mark]
#     arr[right_mark] = temp
#
#     return right_mark

def quick_sort(arr):
    quick_sort_help(arr, 0, len(arr) - 1)


def quick_sort_help(arr, first, last):
    if first < last:
        splitpoint = partition(arr, first, last)

        quick_sort_help(arr, first, splitpoint - 1)
        quick_sort_help(arr, splitpoint + 1, last)


def partition(arr, first, last):
    pivotvalue = arr[first]

    leftmark = first + 1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and arr[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        while arr[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark - 1

        if rightmark < leftmark:
            done = True
        else:
            temp = arr[leftmark]
            arr[leftmark] = arr[rightmark]
            arr[rightmark] = temp

    temp = arr[first]
    arr[first] = arr[rightmark]
    arr[rightmark] = temp

    return rightmark


class TestSearching(unittest.TestCase):

    def setUp(self):
        self.arr = [6,5,2,3,1,8,9,3,4,2,123,3]
        self.sorted_arr = sorted(self.arr)

    def test_bubble_sort(self):
        arr = self.arr[:]
        bubble_sort(arr)
        self.assertEqual(arr, self.sorted_arr)

    def test_selection_sort(self):
        arr = self.arr[:]
        selection_sort(arr)
        self.assertEqual(arr, self.sorted_arr)

    def test_insert_sort(self):
        arr = self.arr[:]
        insert_sort(arr)
        self.assertEqual(arr, self.sorted_arr)

    def test_shell_sort(self):
        arr = self.arr[:]
        shell_sort(arr)
        self.assertEqual(arr, self.sorted_arr)

    def test_merge_sort(self):
        arr = self.arr[:]
        merge_sort(arr)
        self.assertEqual(arr, self.sorted_arr)

    def test_quick_sort(self):
        arr = self.arr[:]
        quick_sort(arr)
        self.assertEqual(arr, self.sorted_arr)

if __name__ == '__main__':
    unittest.main()
