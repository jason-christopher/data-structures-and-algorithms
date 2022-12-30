# Challenge Summary

* Write a function called zip_lists that takes 2 arguments of 2 linked lists and zips the two linked lists together into one so that the nodes alternate between the two lists and return a reference to the the zipped list. Return a new Linked List.

## Whiteboard Process

![White Board CC07](linked_list_zip.png)

## Approach & Efficiency

* Create a new Linked List  called “new_list” using the LinkedList function from the linked_list module.
* Start a “while” loop as long as one of the 2 heads for the 2 input linked lists have a value.
* If the head of the first linked list input has a value, append that value to “new_list” and then change the value of the first linked list’s head to the “next” value.
* If the head of the second linked list input has a value, append that value to “new_list” and then change the value of the second linked list’s head to the “next” value.
* Continue this “while” loop until both input linked lists have no value for their heads.
* Return the new linked list.

Efficiency:
* Time: O(n^2) - quadratic time with nested loops
* Space: O(n) - linear space

## Solution

The solution code is located in the `code_challenges/linked_list_zip.py` file.

1. Within the virtual environment, install pytest via `pip install pytest`.
2. From the Python folder, run tests via `pytest tests/code_challenges/test_linked_list_zip.py`.
3. All 6 tests passed.

## API

* `insert` takes in a `value` sets `self.head` equal to `Node(value, self.head)`. So the head becomes a new `Node` which has a `value` of the input and `next` being the current value of the head.
* `includes` tries to find a input value in the linked list. It takes in a `value` and sets `current` equal to `self.head` and runs a `while` loop until `current` is equal to `None`. If the `current.value` equals the input `value`, then the method returns `True`. If not, the loop sets `current` equal to `current.next` and continues the loop. If the `current` value becomes `None`, then the linked list does not contain the input value and the method returns `False`.
* `__str__` returns the linked list as a string. It sets `current` equal to `self.head`, creates an emtpy `string` variable, and runs a `while` loop until `current` is equal to `None`. While `current` does not equal `None`, then the string is appended with `{ } ->` that contains the `current.value` inside the curly brackets. Once `current` equals `None`, `string` is appended with `NULL`. The `string` variable now contains all values of the linked list and ends with "NULL".
* `append` adds the input value to the end of the list before the `NULL` value.
* `insert_before` adds an inout value before another a specified input.
* `insert_after`adds an inout value before another a specified input.
* `kth_from_end` given an integer `k`, find the value of `k` positions from the end of the linked list.
* `zip_lists` takes 2 arguments of 2 linked lists and zips the two linked lists together into one so that the nodes alternate between the two lists.
