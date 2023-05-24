class TwoStackQueue:
    def __init__(self, max_length=500):
        # Note: can only use append() and pop() on these!
        self.stack1 = []
        self.stack2 = []
        self.num_items = 0
        self.max_length = max_length

    def enqueue(self, item):
        if self.is_full():
            return False

        self.stack1.append(item)
        self.num_items += 1
        return True

    def dequeue(self):
        if self.is_empty():
            return None

        for i in range(len(self.stack1) - 1):
            self.stack2.append(self.stack1.pop())

        removed = self.stack1.pop()

        for i in range(len(self.stack2)):
            self.stack1.append(self.stack2.pop())

        self.num_items -= 1
        return removed

    def front(self):
        if self.is_empty():
            return None

        for i in range(len(self.stack1) - 1):
            self.stack2.append(self.stack1.pop())

        removed = self.stack1.pop()

        # make sure to put the front element back
        self.stack1.append(removed)

        for i in range(len(self.stack2)):
            self.stack1.append(self.stack2.pop())

        return removed

    def is_empty(self):
        return self.num_items == 0

    def is_full(self):
        return self.num_items == self.max_length
