def bubble_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n - 1):
        # Last i elements are already in place
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap if the element found is greater
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
print("Original array:", arr)

bubble_sort(arr)
print("Sorted array:", arr)
