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

            # swapping element at j with element at j
            (array[i], array[j]) = (array[j], array[i])

    # swap the pivot element with the greater element specified by i
    (array[i+1], array[high]) = (array[high], array[i+1])

    return i + 1

# function to perform sorting


def quick_sort(array: list[int], low: int, high: int):
    if low < high:
        # find pivot element so that:
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)

        # recursive call on the left
        quick_sort(array, low, pi - 1)

        # recursive call on the right
        quick_sort(array, pi + 1, high)


data = [8, 7, 2, 1, 0, 9, 6]
print("Unsorted Array")
print(data)

size = len(data)

quick_sort(data, 0, size - 1)

print("sorted data in ascending order")
print(data)
