# 0x01. Lockboxes

This project involves determining whether all the boxes in a set of locked boxes can be opened or not.

## Must Know

For this project, you will need a solid understanding of several key concepts in order to develop a solution that can efficiently determine if all boxes can be opened. Here’s a list of concepts and resources that will be instrumental in tackling this project:

### Concepts Needed:

**Lists and List Manipulation:**
Understanding how to work with lists, including accessing elements, iterating over lists, and modifying lists dynamically.
- [Python Lists (Python Official Documentation)](https://docs.python.org/3/tutorial/datastructures.html)

**Graph Theory Basics:**
Knowledge of graph theory (especially concepts related to traversal algorithms like Depth-First Search or Breadth-First Search) can be very helpful in solving this problem.
- [Graph Theory (Khan Academy)](https://www.khanacademy.org/computing/computer-science/algorithms)

**Algorithmic Complexity:**
Understanding the time and space complexity of your solution is important.
- [Big O Notation (GeeksforGeeks)](https://www.geeksforgeeks.org/analysis-of-algorithms-set-1-asymptotic-analysis/)

**Recursion:**
Some solutions might require a recursive approach to traverse through the boxes and keys.
- [Recursion in Python (Real Python)](https://realpython.com/python-thinking-recursively/)

**Queue and Stack:**
Knowing how to use queues and stacks is crucial if implementing a breadth-first search (BFS) or depth-first search (DFS) algorithm.
- [Python Queue and Stack (GeeksforGeeks)](https://www.geeksforgeeks.org/stack-queue-python-using-module-queue/)

**Set Operations:**
Understanding how to use sets for keeping track of visited boxes and available keys can optimize the search process.
- [Python Sets (Python Official Documentation)](https://docs.python.org/3/tutorial/datastructures.html)

By reviewing these concepts and utilizing these resources, you will be well-equipped to develop an efficient solution for this project, applying both your algorithmic thinking and Python programming skills.

## Requirements

### General:
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/python3
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should be documented
- Your code should use the PEP 8 style (version 1.7.x)
- All your files must be executable

## Tasks

### 0. Lockboxes (mandatory)

You have n number of locked boxes in front of you. Each box is numbered sequentially from 0 to n - 1 and each box may contain keys to the other boxes.

Write a method that determines if all the boxes can be opened.
