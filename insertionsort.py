def insertion_sort(arr):
    # Traverse from 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Move elements greater than key one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Example usage
arr = [64, 25, 12, 22, 11]
print("Original array:", arr)

insertion_sort(arr)
print("Sorted array:", arr)
