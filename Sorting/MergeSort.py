def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)  # Recursively sort the left half
    right_half = merge_sort(right_half) # Recursively sort the right half

    return merge(left_half, right_half) # Merge the sorted halves

def merge(left, right):
    merged_arr = []
    i = 0  # Pointer for left array
    j = 0  # Pointer for right array

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged_arr.append(left[i])
            i += 1
        else:
            merged_arr.append(right[j])
            j += 1

    # Append any remaining elements from left or right arrays
    while i < len(left):
        merged_arr.append(left[i])
        i += 1
    while j < len(right):
        merged_arr.append(right[j])
        j += 1

    return merged_arr

# Example usage:
my_list = [38, 27, 43, 3, 9, 82, 10]
sorted_list = merge_sort(my_list)
print(f"Original list: {my_list}")
print(f"Sorted list: {sorted_list}")


# Original list: [38, 27, 43, 3, 9, 82, 10]
# Sorted list: [3, 9, 10, 27, 38, 43, 82]
