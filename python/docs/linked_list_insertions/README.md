# Challenge Summary

* Write the following methods for the Linked List class:
  * append
    * arguments: new value
    * adds a new node with the given value to the end of the list
  * insert before
    * arguments: value, new value
    * adds a new node with the given new value immediately before the first
    * node that has the value specified
  * insert after
    * arguments: value, new value
    * adds a new node with the given new value immediately after the first node that has the value specified

## Whiteboard Process

![White Board CC06](linked_list_insertions.png)

## Approach & Efficiency

I did the white board for the `append` method of the Linked List function. To insert the input value at the end of the list (before the `NULL` value):
* Set `current` to `self.head`
* Create a `while` loop to run until `current.next` is equal to `None`
  * If not, then set `current` to equal `current.next` and continue the `while` loop
* Once `current.next` is equal to `None`, then set `current.next` to `Node(input)`
* This will add the input value to the end of the list before the `NULL` value.

Efficiency:
* Time: O(n) - linear time since the `while` loop will run for the length of the original Linked List
* Space: O(1) - constant space since the variables do not grow with the length of the Linked List

## Solution

The solution code is located in the `data_structures/linked_list.py` file.

1. Within the virtual environment, install pytest via `pip install pytest`.
2. From the Python folder, run tests via `pytest tests/code_challenges/test_linked_list_insertions.py`.
3. All 8 tests passed.

Example 1:
* Original Linked List: head -> {1} -> {3} -> {2} -> X
* Input: 5
* Output: head -> {1} -> {3} -> {2} -> {5} -> X

Example 2:
* Original Linked List: head -> X
* Input: 1
* Output: head -> {1} -> X
