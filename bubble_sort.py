array = [1, 6, 3, 4, 2, 8]

def bubble_sort(array):
    length = len(array)

    for i in range(length):
        # adjusting the length of which we actually have to swap the numbers.
        # as i increases, the last i elements will be sorted, and therefore
        # we need to loop through less elements in the list
        for j in range(0, length-i-1):

            # if the current element is larger than the next element,
            # swap the two in the list
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    return array

sorted_array = bubble_sort(array)
print(sorted_array)