def linear_search(arr, target):
    # Traverse the array
    for i in range(len(arr)):
        if arr[i] == target:
            return i   # return index if found
    return -1          # return -1 if not found

# Example usage
arr = [64, 25, 12, 22, 11]
target = 22

print("Array:", arr)
result = linear_search(arr, target)

if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print(f"Element {target} not found")
