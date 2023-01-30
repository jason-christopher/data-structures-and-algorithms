# Hash Tables

A hash table, also known as a hash map, is a data structure that stores key-value pairs, where each key is mapped to a specific value using a hash function. The hash function takes the key as input and produces an index, called a "hash value," that corresponds to a specific position in the table, where the associated value can be found.

## Challenge

Implement a Hashtable Class with the following methods:
* `set(key, value)` - returns nothing
  * This method should hash the key, and set the key and value pair in the table, handling collisions as needed.
  * Should a given key already exist, replace its value from the value argument given to this method.
* `get(key)` - return the value associated with that key in the table
* `has(key)` - returns a Boolean indicating if the key exists in the table already.
* `keys()` - returns a list of keys
* `hash(key)` - returns the index in the collection for that key

## Efficiency

Efficiency:
* Time: O(n) - Linear time
* Space: O(n) - Linear space

## API

* `set(key, value)` - sets the key and value pair in the table, handling collisions as needed.
* `get(key)` - returns the value associated with that key in the table
* `has(key)` - returns a Boolean indicating if the key exists in the table already.
* `keys()` - returns a list of keys
* `hash(key)` - returns the index in the collection for that key

## Solutions & Tests

* [Solution Code](../../data_structures/hashtable.py)
* [Tests](../../tests/data_structures/test_hashtable.py)

## Links & Resources

* [Code Fellows Reading](https://codefellows.github.io/common_curriculum/data_structures_and_algorithms/Code_401/class-30/resources/Hashtables.html)
