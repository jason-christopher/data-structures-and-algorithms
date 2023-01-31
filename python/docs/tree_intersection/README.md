# Challenge Summary

* Write a function called `tree_intersection` that takes two binary trees as parameters. Using your `Hashmap` implementation as a part of your algorithm, return a set of values found in both trees.

## Whiteboard Process

![Tree Intersection](tree_intersection.png)

## Approach & Efficiency

Approach
* Create an empty list called ‘result’ and create an empty Hash Table called ‘diction’.
* Define a ‘walk’ function that will be called recursively that takes in a ‘root’ node and a boolean based on if the tree is the first tree ot not.
  * If it’s the first tree, add the node’s value to the Hash Table (using the ‘set’ method).
  * If it’s NOT the first tree AND the input node’s value is in the Hash Table (using the ‘has’ method), append the value to ‘result’.
  * If the node has a ‘left’ node, recursively call that that node.
  * If the node has a ‘right node, recursively call that that node.
* Pass in the first binary tree’s root into the ‘walk’ function with a True value for ‘first’.
* Pass in the second binary tree’s root into the ‘walk’ function with a False value for ‘first’.
* Return ‘result’ as a set to remove duplicates.

Efficiency
* Time: O(n) - linear time to ‘walk’ through binary trees.
* Space: O(n) - linear space if both trees have the same values.

## Solution

The solution code is located in the `code_challenges/tree_intersection.py` file.

1. Within the virtual environment, install pytest via `pip install pytest`.
2. From the Python folder, run tests via `pytest tests/code_challenges/test_tree_intersection.py`.
3. All 4 tests passed.
