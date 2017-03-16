def pair_sum(arr, k):

    pairs = []

    for i, elem1 in enumerate(arr):
        for elem2 in arr[i+1:]:
            if elem1 + elem2 == k:
                pairs.append((elem1,elem2))

    print(pairs)

# pair_sum([1,3,2,2], 4)


def correct_pair(arr, k):

    if len(arr) < 2:
        return

    seen = set()
    output = set()

    for num in arr:

        target = k - num

        if target not in seen:
            seen.add(num)

        else:
            output.add((min(num, target), max(num, target)))

    print('\n'.join(map(str, list(output))))

correct_pair([1,3,2,2], 4)
