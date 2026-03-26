# Data structures - unit 1 assignment

*Submitted for college evaluation.*

## Student information

**Subject:** Data structures  
**Assignment:** Unit 1  
**Name:** Harsh Dev Jha  
**ID:** 2501010168  
**Section:** B.Tech CSE CORE SEC-A  
**Semester:** 2nd  

---

## Project overview

This assignment covers recursion and searching. It includes some common math problems and search algorithms along with their complexity analysis. Everything is written in Python.

---

## Question 1: Recursive factorial
**File:** `q1_factorial.py`

The factorial of a number is the product of all positive integers up to that number. I've included two ways to do this:
- Naive recursion: This follows the math definition.
- Memoization: This uses a cache to make it faster by not repeating calculations.
- Complexity: Time is O(n) and space is O(n).

---

## Question 2: Recursive fibonacci
**File:** `q2_fibonacci.py`

The fibonacci sequence is where each number is the sum of the last two. This script compares a standard recursive approach with a memoized one.
- Performance: The naive method is very slow for bigger numbers.
- Optimization: A simple dictionary cache makes it much faster, even for n=100.
- Complexity: Naive is O(2^n) and memoized is O(n).

---

## Question 3: Tower of hanoi
**File:** `q3_tower_of_hanoi.py`

Tower of hanoi is a puzzle with three rods and different sized disks. The goal is to move the stack from one rod to another without ever putting a bigger disk on a smaller one.
- Implementation: This uses a divide and conquer strategy.
- Analysis: I've included a trace for 3 disks to show how it works.
- Complexity: Time is O(2^n) and space is O(n).

---

## Question 4: Recursive binary search
**File:** `q4_binary_search.py`

Binary search is a way to find a value in a sorted list by splitting the search area in half each time.
- Logic: It checks the middle, then decides which half to search next.
- Analysis: I used the master theorem to show why it's efficient.
- Complexity: Time is O(log n) and space is O(log n).

---

## Documentation
- `explanation.md`: Technical details and traces for the assignment.

## How to run
Make sure you have Python 3 installed. You can run the files like this:
```bash
python q1_factorial.py
python q2_fibonacci.py
python q3_tower_of_hanoi.py
python q4_binary_search.py
```

---
