# Challenge Summary

* Node
  * Create a Node class that has properties for the value stored in the Node, and a pointer to the next Node.
* Linked List
  * Create a Linked List class
    * Within your Linked List class, include a head property.
    * Upon instantiation, an empty Linked List should be created.
    * The class should contain the following methods
      * insert
        * Arguments: value
        * Returns: nothing
        * Adds a new node with that value to the head of the list with an O(1) Time performance.
      * includes
        * Arguments: value
        * Returns: Boolean
          * Indicates whether that value exists as a Node’s value somewhere within the list.
      * to string
        * Arguments: none
        * Returns: a string representing all the values in the Linked List, formatted as: "{ a } -> { b } -> { c } -> NULL"

## Whiteboard Process

* No whiteboard required for this Code Challenge

## Approach & Efficiency

Node
* Created a `Node` class that takes in a `value` and a `next` and sets `self.value` equal to `value` and sets `self.next` equal to `next`. If there is no `next` passed in, the default value of `next` is `None`.

Linked List
* Created a `LinkedList` class that has a `__init__` that initially sets `self.head` equal to `None` and also has 3 methods: `insert`, `includes`, and `__str__`:
  * `insert` takes in a `value` sets `self.head` equal to `Node(value, self.head)`. So the head becomes a new `Node` which has a `value` of the input and `next` being the current value of the head.
  * `includes` tries to find a input value in the linked list. It takes in a `value` and sets `current` equal to `self.head` and runs a `while` loop until `current` is equal to `None`. If the `current.value` equals the input `value`, then the method returns `True`. If not, the loop sets `current` equal to `current.next` and continues the loop. If the `current` value becomes `None`, then the linked list does not contain the input value and the method returns `False`.
  * `__str__` returns the linked list as a string. It sets `current` equal to `self.head`, creates an emtpy `string` variable, and runs a `while` loop until `current` is equal to `None`. While `current` does not equal `None`, then the string is appended with `{ } ->` that contains the `current.value` inside the curly brackets. Once `current` equals `None`, `string` is appended with `NULL`. The `string` variable now contains all values of the linked list and ends with "NULL".

Efficiency:
* Time: O(n) - linear time since the `while` loop will run for the length of the original Linked List
* Space: O(1) - constant space since the variables do not grow with the length of the Linked List

## Solution

The solution code is located in the `data_structures/linked_list.py` file.

1. Within the virtual environment, install pytest via `pip install pytest`.
2. From the Python folder, run tests via `pytest tests/data_structures/test_linked_list.py`.
3. All 9 tests passed.

Insert Example:
* Original Linked List: {1} -> {3} -> {2} -> X
* Input: 5
* Output: {5} -> {1} -> {3} -> {2} -> X

Includes Example:
* Original Linked List: {1} -> {3} -> {2} -> X
* Input: 3
* Output: True

To String Example:
* Original Linked List: {1} -> {3} -> {2} -> X
* Output: "{ 1 } -> { 3 } -> { 2 } -> NULL"

## API

* `insert` takes in a `value` sets `self.head` equal to `Node(value, self.head)`. So the head becomes a new `Node` which has a `value` of the input and `next` being the current value of the head.
* `includes` tries to find a input value in the linked list. It takes in a `value` and sets `current` equal to `self.head` and runs a `while` loop until `current` is equal to `None`. If the `current.value` equals the input `value`, then the method returns `True`. If not, the loop sets `current` equal to `current.next` and continues the loop. If the `current` value becomes `None`, then the linked list does not contain the input value and the method returns `False`.
* `__str__` returns the linked list as a string. It sets `current` equal to `self.head`, creates an emtpy `string` variable, and runs a `while` loop until `current` is equal to `None`. While `current` does not equal `None`, then the string is appended with `{ } ->` that contains the `current.value` inside the curly brackets. Once `current` equals `None`, `string` is appended with `NULL`. The `string` variable now contains all values of the linked list and ends with "NULL".
