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
    pass


def insert_sort(arr):
    pass


arr = [6,5,2,3,1,8,9,3,4,2,0,123,3]
# bubble_sort(arr)
selection_sort(arr)
print(arr)