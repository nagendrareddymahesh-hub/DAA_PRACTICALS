def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Find the middle
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursively sort both halves
        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        # Merge the sorted halves
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Copy remaining elements of left_half
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Copy remaining elements of right_half
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Example usage
arr = [64, 25, 12, 22, 11]
print("Original array:", arr)

merge_sort(arr)
print("Sorted array:", arr)
