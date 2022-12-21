# Insert to Middle of an Array

Write a function called reverseArray which takes an array as an argument. Without utilizing any of the built-in methods available to your language, return an array with elements in reversed order.

## Whiteboard Process

![CC02 Whiteboard](./array_insert_shift.png)

## Approach & Efficiency

I found the length of the input list and divided by 2 (rounding down using the // floor division operator) and saved the number to a variable called "location". Then I returned a new list that concatenated the first half of the input list, the input number, then the last half of the input list using ":"'s to divide the original list.

Efficiency is O(1) for time since it will remain constant and O(N) for space since it will increase linearly.
