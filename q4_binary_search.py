"""
q4 recursive binary search implementation
"""

def binary_search_recursive(arr, low, high, target):
    """
    performs recursive binary search on a sorted list.
    arr: sorted list
    low: start index
    high: end index
    target: what we're looking for
    returns: the index if found, or -1
    """
    if low <= high:
        mid = (low + high) // 2

        # if it's at the middle
        if arr[mid] == target:
            return mid

        # if it's smaller than mid, check left half
        elif arr[mid] > target:
            return binary_search_recursive(arr, low, mid - 1, target)

        # if it's larger than mid, check right half
        else:
            return binary_search_recursive(arr, mid + 1, high, target)

    # base case when target isn't there
    return -1


# complexity notes
"""
time complexity:
binary search splits the list in half each time. 
the recurrence is T(n) = T(n/2) + O(1).
using the master theorem, this comes out to O(log n).

space complexity:
it's O(log n) because of the recursion stack depth.
"""

def main():
    sorted_array = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    target_val = 23
    
    print(f"--- q4 recursive binary search ---")
    print(f"array: {sorted_array}")
    print(f"target: {target_val}")
    
    result = binary_search_recursive(sorted_array, 0, len(sorted_array) - 1, target_val)
    
    if result != -1:
        print(f"found at index: {result}")
    else:
        print("not found.")

if __name__ == "__main__":
    main()
