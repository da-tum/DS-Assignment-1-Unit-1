"""
q3 tower of hanoi implementation
"""

def tower_of_hanoi(n, source, destination, auxiliary):
    """
    recursive function for the tower of hanoi puzzle.
    n: number of disks
    source: start rod
    destination: end rod
    auxiliary: helper rod
    """
    if n == 1:
        print(f"move disk 1 from {source} to {destination}")
        return

    # move n-1 disks from source to auxiliary
    tower_of_hanoi(n - 1, source, auxiliary, destination)
    
    # move the n-th disk from source to destination
    print(f"move disk {n} from {source} to {destination}")
    
    # move n-1 disks from auxiliary to destination
    tower_of_hanoi(n - 1, auxiliary, destination, source)


# step by step trace for 3 disks
"""
trace for n=3 (source: a, destination: c, auxiliary: b):

hanoi(3, 'A', 'C', 'B'):
1. move disk 1 from A to C
2. move disk 2 from A to B
3. move disk 1 from C to B
4. move disk 3 from A to C
5. move disk 1 from B to A
6. move disk 2 from B to C
7. move disk 1 from A to C

total steps: 7 (which is 2^3 - 1)
"""

# complexity notes
"""
time complexity:
the number of moves for n disks follows the rule T(n) = 2*T(n - 1) + 1.
if you expand this out, it's a geometric progression that sums to 2^n - 1.
so the time complexity is O(2^n).

space complexity:
it's O(n) because of the recursion stack depth.
"""

def main():
    n = 3
    print(f"--- q3 tower of hanoi (n={n}) ---")
    tower_of_hanoi(n, 'A', 'C', 'B')

if __name__ == "__main__":
    main()
