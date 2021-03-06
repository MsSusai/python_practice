def quickSort(alist):
    quickSortHelper(alist, 0, len(alist) - 1)


def quickSortHelper(alist, first, last):
    if first < last:
        splitPoint = partition(alist, first, last)
        quickSortHelper(alist, first, splitPoint - 1)
        quickSortHelper(alist, splitPoint + 1, last)


def partition(alist, first, last):
    pivotValue = alist[first]

    left = first + 1
    right = last

    done = False
    while not done:
        while alist[left] <= pivotValue and left <= right:
            left += 1
        while alist[right] >= pivotValue and left <= right:
            right -= 1
        if right < left:
            done = True
        else:
            alist[left], alist[right] = alist[right], alist[left]

    alist[first], alist[right] = alist[right], alist[first]
    return right


# pythonic
def quick_sort(alist):
    if len(alist) <= 1:
        return alist
    else:
        mid = len(alist) // 2
        left, right = [], []
        splitValue = alist[mid]
        alist.remove(splitValue)

        for num in alist:
            if num < splitValue:
                left.append(num)
            else:
                right.append(num)
        return quick_sort(left) + [splitValue] + quick_sort(right)


test = [1, 5, 6, 2, 3, 2, 6, 7, 9, 10]
print(quick_sort(test))
# quickSort(test)
# print(test)

