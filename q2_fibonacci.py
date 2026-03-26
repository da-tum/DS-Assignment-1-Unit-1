"""
q2 fibonacci implementation
"""

# basic recursion for fibonacci
def fibonacci_naive(n):
    """
    finds n-th fibonacci number with regular recursion.
    this is really slow for large n.
    time: O(2^n), space: O(n)
    """
    if n <= 1:
        return n
    return fibonacci_naive(n - 1) + fibonacci_naive(n - 2)


# memoized version to speed it up
fib_cache = {0: 0, 1: 1}

def fibonacci_memoized(n):
    """
    uses a cache so we don't recalculate things.
    time: O(n), space: O(n)
    """
    if n in fib_cache:
        return fib_cache[n]
    
    fib_cache[n] = fibonacci_memoized(n - 1) + fibonacci_memoized(n - 2)
    return fib_cache[n]


# notes on efficiency
"""
why the naive version is slow:
it solves the same subproblems over and over. for example, to find fib(5),
it calculates fib(3) twice and fib(2) three times.
this makes the time complexity exponential, O(2^n).

why memoization helps:
every number from 0 to n is only calculated once and stored in the dictionary.
this brings the time complexity down to O(n).
space is also O(n) for the cache and the recursion stack.
"""

def main():
    test_val = 10
    print(f"--- q2 fibonacci (n={test_val}) ---")
    print(f"naive result: {fibonacci_naive(test_val)}")
    print(f"memoized result: {fibonacci_memoized(test_val)}")
    print("for n=35, naive would be slow, but memoized is fast.")

if __name__ == "__main__":
    main()
