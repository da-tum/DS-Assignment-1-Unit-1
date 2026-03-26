"""
q1 factorial implementation
"""

import sys

# increasing recursion limit just in case
sys.setrecursionlimit(2000)

# basic recursive factorial
def factorial_naive(n):
    """
    uses standard recursion to find factorial.
    time: O(n), space: O(n)
    """
    if n == 0 or n == 1:
        return 1
    return n * factorial_naive(n - 1)


# optimized version with a cache
factorial_cache = {0: 1, 1: 1}

def factorial_memoized(n):
    """
    uses a dictionary to skip repeats.
    time: O(n) first time, O(1) after.
    space: O(n)
    """
    if n in factorial_cache:
        return factorial_cache[n]
    
    factorial_cache[n] = n * factorial_memoized(n - 1)
    return factorial_cache[n]


# complexity notes
"""
time complexity:
both ways are O(n) because of the n recursive calls.
memoization is better if we call it many times since it saves old results.

space complexity:
naive is O(n) for the call stack. 
memoized is also O(n) for the stack and the dictionary.
"""

def main():
    test_val = 10
    print(f"--- q1 factorial (n={test_val}) ---")
    print(f"naive result: {factorial_naive(test_val)}")
    print(f"memoized result: {factorial_memoized(test_val)}")
    print(f"cache entries: {len(factorial_cache)}")

if __name__ == "__main__":
    main()
