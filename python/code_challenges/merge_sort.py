def merge_sort(list):
    n = len(list)
    if n > 1:
        mid = n//2
        left = list[:mid]
        right = list[mid:]
        # sort the left side
        merge_sort(left)
        # sort the right side
        merge_sort(right)
        # merge the sorted left and right sides together
        merge(left, right, list)
    return list


def merge(left, right, list):
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            list[k] = left[i]
            i += 1
        else:
            list[k] = right[j]
            j = j + 1
        k += 1
    if i == len(left):
        list[k:] = right[j:]
    else:
        list[k:] = left[i:]
    return list
