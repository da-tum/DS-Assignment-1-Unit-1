# Technical explanation - unit 1 assignment

This document has a breakdown of the recursive algorithms in this assignment, including traces and complexity notes.

---

## 1. Recursive factorial (q1)

### Ways to do it:
- Naive recursion: Uses the standard rule $F(n) = n \times F(n-1)$.
- Memoized recursion: Uses a dictionary to save old values so we don't repeat work.

### Complexity:
- Time complexity: O(n) for both. Memoization is O(1) if we call it again with the same number.
- Space complexity: O(n) because of the recursion stack depth.

---

## 2. Recursive fibonacci (q2)

### Why naive recursion is slow:
In the naive way where $F(n) = F(n-1) + F(n-2)$, the same problems are solved many times. For example, to find $F(5)$ we end up finding $F(3)$ twice and $F(2)$ three times. This makes the calls grow very fast.

### Complexity:
- Naive time: O(2^n).
- Memoized time: O(n) because each value is only found once.
- Space complexity: O(n) for the stack and the cache.

---

## 3. Tower of hanoi (q3)

### Trace for 3 disks:
Steps to move 3 disks from A to C using B:
1. move disk 1 from A to C
2. move disk 2 from A to B
3. move disk 1 from C to B
4. move disk 3 from A to C
5. move disk 1 from B to A
6. move disk 2 from B to C
7. move disk 1 from A to C

### Complexity:
The rule is $T(n) = 2T(n-1) + 1$. This works out to $T(n) = 2^n - 1$.
- Time complexity: O(2^n).
- Space complexity: O(n) for stack depth.

---

## 4. Recursive binary search (q4)

### Complexity:
The search area is cut in half every time: $T(n) = T(n/2) + O(1)$.

### Master theorem:
$T(n) = aT(n/b) + f(n)$ where $a=1, b=2, f(n)=1$.
$n^{\log_b a} = n^{\log_2 1} = 1$.
Since $f(n)$ is constant, we use case 2 of the master theorem.
- Time complexity: O(log n).

### Space complexity:
O(log n) because the stack depth depends on the number of splits.
