import collections


def finder(arr1, arr2):

    for elem in arr2:
        try:
            arr1.remove(elem)
        except ValueError:
            print('Ups!')

    return arr1[0]


def finder2(arr1, arr2):
    arr1.sort()
    arr2.sort()

    for num1, num2 in zip(arr1, arr2):
        if num1 != num2:
            return num1

    return arr1[-1]


def finder3(arr1, arr2):
    d = collections.defaultdict(int)

    for num in arr2:
        d[num] += 1

    for num in arr1:
        if d[num] == 0:
            return num
        else:
            d[num] -= 1

def finder4(arr1, arr2):
    return sum(arr1) - sum(arr2)


def clever_trick(arr1, arr2):
    result = 0

    for num in arr1 + arr2:
        result^=num
        print(result)

    return result

print(finder2([1,2,3,4,5,6,7], [3,7,2,1,4,6]))