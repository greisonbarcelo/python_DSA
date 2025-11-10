def partition(array, low, high):  # ([4, 1, 3, 6], 0, 2)
    pivot = array[high]  # pivot = 3
    i = low - 1  # i = -1

    for j in range(low, high):  # (1, 2)
        if array[j] <= pivot:  # array[1] = 1 <= 3 True
            i += 1  # i = 0
            array[i], array[j] = array[j], array[i]
            # [0][1] = [1][0] => [1, 4, 3, 6] but i = 0
            # stops at low = 1, high = 2
    array[i+1], array[high] = array[high], array[i+1]
    # [1][2] = [2][1] = [1, 3, 4, 6]
    print(mylist)
    return i+1  # 2+1 = 3


def quicksort(array, low=0, high=None):
    if high is None:
        high = len(array) - 1  # high = 3

    if low < high:  # 0, 2 True
        pivot_index = partition(array, low, high)
        # ([4, 1, 3, 6], 0, 3) pivot_index = 3
        quicksort(array, low, pivot_index-1)
        # ([4, 1, 3, 6], 0, 2)
        quicksort(array, pivot_index+1, high)
        # ([4, 1, 3, 6], 0, 2) => [1, 3, 4, 6]


mylist = [4, 1, 3, 6]

quicksort(mylist)
