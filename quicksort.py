def partition(array: list[int], low: int, high: int):
    # Choose rightmost as pivot
    pivot = array[high]

    # First pointer (for greater element)
    i = low - 1

    # Iterate through elements
    for j in range(low, high):
        if array[j] <= pivot:
            # If element smaller than pivot is found
            # then we swap it with the greater element pointed by i
            i = i + 1
    pass
