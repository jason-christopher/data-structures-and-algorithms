# Stacks and Queues

A stack's topmost item is denoted as the top. When you push something to the stack, it becomes the new top. When you pop something from the stack, you pop the current top and set the next top as top.next. Stacks utilize the First In, Last Out (FILO) and the Last In, First Out (LIFO) concept. A queue's'front-most item is denoted as the front.

When you enqueue something to the queue, it becomes the new back item. When you dequeue something from the queue, you remove the current front and set the next front as front.next. Queues utilize the First In, First Out (FIFO) and the Last In, Last Out (LILO) concept.

# Challenge Summary

* Implement both a Stack and a Queue
  * Node
    * Create a `Node` class that has properties for the `value` stored in the Node, and a pointer to the `next` node.
  * Stack
    * Create a `Stack` class that has a `top` property. It creates an empty `Stack` when instantiated. This object should be aware of a default empty value assigned to top when the stack is created. The class should contain the following methods: `push`, `pop`, `peek`, and `is_empty`.
  * Queue
    * Create a `Queue` class that has a `front` property. It creates an empty `Queue` when instantiated. This object should be aware of a default empty value assigned to front when the queue is created. The class should contain the following methods: `enqueue`, `dequeue`, `peek`, and `is_empty`.

## Whiteboard Process

* No whiteboard required.

## Approach & Efficiency

Stack

* `__init__` - creates an empty stack with a `top` of `None`.
* `push` - Requires a `value` input and adds a new node with that `value` to the `top` of the stack. It sets the new node's `next` and the current `top`'s node.
* `pop` - Returns the `value` from the node at the `top` of the stack. Sets the current's `top`'s `next` as the current `top`'s `next`. Raises an exception when called on empty stack.
* `peek` - Returns the `value` of the node located at the `top` of the stack. Raises an exception when called on an empty stack.
* `is-empty` - Returns a Boolean indicating whether the stack is empty by seeing the `top`'s value is `None`.

Queue

* `__init__` - creates an empty queue with a `front` and `back` of `None`.
* `enqueue` - If there is a `back` then it sets its `next` equal to a new node with the input `value` and then sets `back` equal to the new node. If the queue is empty, it sets front and back equal to the new node.
* `dequeue` - Removes and returns the `value` from node from the `front` of the queue and sets `front` equal to the current `front`'s `next`. Raises an exception when called on empty queue.
* `peek` - Returns a `value` of the node located at the `front` of the queue or raises an exception when called on an empty queue.
* `is-empty` - Returns a Boolean indicating whether the queue is empty by seeing the `front`'s value is `None`.

Efficiency:
* It depends with the different methods, but many are O(1) for time and space because they are constant with time and space. That is one of the advantages of using these Node-based data structures.

## Solution

The solution code is located in the `data_structures/stack.py` file and `data_structures/queue.py` file.

1. Within the virtual environment, install pytest via `pip install pytest`.
2. From the Python folder, run tests via `pytest tests/data_structures/test_stack.py` and `pytest tests/data_structures/test_queue.py`.
3. All 9 tests passed for stack and all 12 tests passed for queue.

## API

Stack

* `__init__` - creates an empty stack with a `top` of `None`.
* `push` - Requires a `value` input and adds a new node with that `value` to the `top` of the stack with an O(1) Time performance.
* `pop` - Removes the node from the `top` of the stack and returns the `value` from that node or raises an exception when called on empty stack.
* `peek` - Returns the `value` of the node located at the `top` of the stack or raises an exception when called on an empty stack.
* `is-empty` - Returns a Boolean indicating whether the stack is empty.

Queue

* `__init__` - creates an empty queue with a `front` and `back` of `None`.
* `enqueue` - Requires a `value` input and adds a new node with that `value` to the `back` of the queue with an O(1) Time performance.
* `dequeue` - Removes and returns the `value` from node from the `front` of the queue or raises an exception when called on empty queue.
* `peek` - Returns a `value` of the node located at the `front` of the queue or raises an exception when called on an empty queue.
* `is_empty` - Returns a Boolean indicating whether the queue is empty.
