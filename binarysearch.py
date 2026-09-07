def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2   # middle index
        if arr[mid] == target:
            return mid            # element found
        elif arr[mid] < target:
            low = mid + 1         # search right half
        else:
            high = mid - 1        # search left half
    return -1                     # not found

# Example usage
arr = [11, 12, 22, 25, 64]   # must be sorted
target = 22

print("Array:", arr)
result = binary_search(arr, target)

if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print(f"Element {target} not found")
