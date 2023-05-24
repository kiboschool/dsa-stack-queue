# Two Stack Queue

In this practice, you will implement the queue ADT using two stacks.

## Starter Code

You are given the file `twostackqueue.py`, which includes a skeleton implementation of the `TwoStackQueue` class. This class implements the queue ADT and therefore holds stubs for the following methods:

* `enqueue()`: add an item at the rear of the queue
* `dequeue()`: remove the item at the front of the queue
* `front()`: get the item at the front of the queue, but don't remove it
* `is_empty()`: test if the queue is empty
* `is_full()`: test if the queue is full

***You should not change any of the existing methods in the `TwoStackQueue` class.***

## Approach

The goal of this exercise is to become familiar with the semantics and behavior of stacks and queues.

To implement the queue ADT, you are only allowed to use exactly **two** stack data structures. Aside from these two stacks, the methods you write may use only a constant amount of additional memory -- which means you cannot use additional lists, dictionaries, or other data structures.

There are multiple ways to approach this problem. Here are two suggested techniques:

1. On `enqueue()`, just put everything into the first stack. The first stack will essentially hold the items of the queue in reverse order. On `dequeue()`, the item that should be removed is at the *bottom* of the first stack. You will need to use the second stack in order to get it and then restore the first stack back to its original order.

2. On `enqueue()`, do extra work to ensure that the next element that might be `dequeued()` is at the *top* of the first stack. Doing so may make `enqueue()` more computationally expensive, but will make `dequeue() easier.

Instead of using oen of the stack classes that we implemented in the lessons (`ArrayStack` or `LLStack`), for your stacks you should use Python lists. However, you are *not* allowed to index the lists (`self.stack1[i]` for any value `i`), as stacks do not support that operation. Instead, you can only use:

* `self.stack.append()`: to "push" an item onto the stack
* `self.stack.pop()`: to "pop" an item from the stack

## Steps to Complete

Your task is to implement the methods of the queue ADT in the `TwoStackQueue` class. Remember the above guidelines:

1. You can only use `self.stack1` and `self.stack2` -- no additional data structures.
2. The stacks are Python lists, but you can only use the following methods: `append()` and `pop()`.

Start with the two easiest methods first:

1. `is_empty()`

    The `is_empty()` method should return whether the queue is empty. For this task, you should consult the value of `self.num_items`.

2. `is_full()`

    The `is_full()` method should return whether the queue is full. For this task, you should consult the value of the variables `self.num_items` and `self.max_items`.

Once those methods are done, you can move on to the three slightly harder methods:

3. `enqueue()`

    The `enqueue()` method should first check whether the queue is full, and if it is, return `False` and do not enqueue the item.

    Otherwise, `enqueue()` should enqueue an item using one or both stacks, depending on the approach that you take to solving the problem. Remember to increment the number of items.

4. `dequeue()`

    The `dequeue()` method should first check whether the queue is empty, and if it is, return `None`.

    Otherwise, `dequeue()` should dqueue an item using one or both stacks, depending on the approach that you take to solving the problem. Remember to decrement the number of items.

5. `front()`

    The `front()` method should return the item at the front of the queue, but should *not* actually remove the item. You may need to temporarily alter the contents of the stacks in order to find the item that's at the front of the queue, but by the time the `front()` method returns the state of the queue (i.e., the stacks) should be restored to their previous state.

## Testing

In `test_twostackqueue.py`, there are unit tests that cover each of the five methods described above.
