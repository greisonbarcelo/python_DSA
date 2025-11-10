def partition(array, low, high):  # partition([3, 2, 5, 7], 0, 1)
    pivot = array[high]  # pivot array[1] = 2
    i = low - 1  # i = -1

    for j in range(low, high):  # (0, 1)
        if array[j] <= pivot:  # array[0] = 3 <= pivot [1] = 2: False
            i += 1  #
            array[i], array[j] = array[j], array[i]
            # SKIP array [1] [2] = [2] [1] swap = [3, 2, 7, 5] stops loop because it cannot low = high

    array[i+1], array[high] = array[high], array[i+1]
    # [0][1] = [1][0] = [2, 3, 5, 7]
    # SKIP array [2] [3] = [3] [2] swap = [3, 2, 5, 7]
    return i+1  # -1+1 = 0


def quicksort(array, low=0, high=None):  # quicksort([3, 7, 2, 5], 0, None)
    if high is None:
        high = len(array) - 1  # quicksort([3, 7, 2, 5], 0, 3)

    if low < high:  # 0 < 5 = True
        # partition([3, 7, 2, 5], 0, 3)
        pivot_index = partition(array, low, high)  # pivot_index = 2
        # ([3, 2, 5, 7], 0, 1) => [2, 3, 5, 7]
        quicksort(array, low, pivot_index-1)
        quicksort(array, pivot_index+1, high)  # ([2, 3, 5, 7], 3, 3)


mylist = [3, 7, 2, 5, 1, 4, 6]
print(mylist)
quicksort(mylist)
print(mylist)
