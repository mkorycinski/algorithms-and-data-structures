def sequential_search_unord(term, arr):
    i = 0
    found = False

    while i < len(arr) and not found:
        if arr[i] == term:
            found = True
        else:
            i += 1

    return False


def sequential_search_ordered(term, arr):

    i = 0
    found = False
    stopped = False

    while i < len(arr) and not found and not stopped:

        if arr[i] == term:
            found = True

        elif arr[i] > term:
            stopped = True

        else:
            i += 1


if __name__ == '__main__':

    arr = list(map(int, list('189279391')))

    ordered_arr = list(map(int, list('123456789')))

    print(sequential_search_unord(5, arr))
    print(sequential_search_unord(9, arr))

    print(sequential_search_ordered(5, ordered_arr))
    print(sequential_search_ordered(10, ordered_arr))