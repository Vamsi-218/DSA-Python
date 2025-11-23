# IDEA:: 
# Larger element bubbles-up to end of list during each pass by just comparing with adjacent element

## Implementation of Bubble Sort

# Stable Algo
# Inplace Algo
# Comparison - Based
## Time complexity: O(n^2)

## Method implementation
def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            # (0, n-i-1)
            if arr[j] > arr[j+1]:
                ## swap of the elements
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

## Driver code
arr = [70, 20, 50, 60, 35, 47]
result = bubbleSort(arr)
print("Array after using bubble sort is:", result)


# Optimised:: Takes O(N) If array is already sorted
def bubbleSortOpt(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            # (0, n-i-1)
            if arr[j] > arr[j+1]:
                ## swap of the elements
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if (not swapped): # Already swapped
            # (swapped == False)
            break
    return arr

## Driver code
arr = [10, 20, 30, 60]
result = bubbleSortOpt(arr)
print("Array after using bubble sort is:", result)



# To check if swap happened or not
def bubble_sort_optimized(arr: list) -> None:
    """
    In-place optimized bubble sort (ascending).
    Now prints whether a swap happened in each pass.
    """
    n = len(arr)
    for i in range(n):
        swapped = False
        print(f"\nPass {i + 1}:")   # pass count starting from 1

        # After i passes, last i items are in final position
        for j in range(0, n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if swapped:
            print("  Swap happened")
        else:
            print("  No swap — array is already sorted")
            break
    return arr
arr = [1,2,3,4]
bubble_sort_optimized(arr)
