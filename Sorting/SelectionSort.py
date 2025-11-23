## IDEA::
# We have min variable to store index of min element from unsorted part and moves it to begining 

## Implementation of the selection sort

# Stability : Unstable
# Inplace
# Comparision based

## Time complexity: O(n^2)
## Method Definition
def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            # (i+1, n)
            # find min element in array
            if arr[j] < arr[min_idx]:
                min_idx = j
        ## swap happened after every pass
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

## Driver code
arr = [70, 56, 23, 19, 25, 37, 48]
result = selectionSort(arr)
print("Sorted array after applying selection sort:", result)

# Why selection sort is unstable ??
# arr = [4a, 4b, 2]
# min_element = 2
# so we swap 4a, 2 positions
# Now array becomes [2, 4b, 4a] where it doesn't maintain their relative order....



# How to make selection sort Stable ??
# 🔧 Key idea:

# Instead of swapping the minimum element with arr[i],
# we:
# Store the minimum value
# Shift all elements between i and min_index right by 1
# Insert the minimum element at position i
# This way, equal elements keep their original order.

def stable_selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i

        # Find index of minimum element
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Extract the minimum element
        key = arr[min_index]

        # Shift elements right instead of swapping
        while min_index > i:
            arr[min_index] = arr[min_index - 1]
            min_index -= 1

        # Place the minimum element at its correct position
        arr[i] = key
    return arr
arr = [70, 56, 23, 19, 25, 37, 48]
res = stable_selection_sort(arr)
print(res)
