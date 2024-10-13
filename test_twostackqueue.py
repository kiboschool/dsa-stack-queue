import unittest
import io
import sys
from twostackqueue import TwoStackQueue

class TestTwoStackQueue(unittest.TestCase):
    def setUp(self):
        self.q = TwoStackQueue(5)

    def test_enqueue(self):
        assert self.q.is_empty()
        assert self.q.enqueue(1)
        assert self.q.enqueue(2)
        assert self.q.enqueue(3)
        assert self.q.enqueue(4)
        assert not self.q.is_full()
        assert self.q.enqueue(5)
        assert not self.q.is_empty()
        assert self.q.is_full()
        assert not self.q.enqueue(6)

    def test_dequeue(self):
        assert self.q.enqueue(1)
        assert self.q.enqueue(2)
        assert self.q.enqueue(3)
        assert self.q.dequeue() == 1
        assert self.q.dequeue() == 2
        assert self.q.dequeue() == 3

    def test_dequeue_empty(self):
        assert self.q.enqueue(1)
        assert self.q.enqueue(2)
        assert self.q.enqueue(3)
        assert self.q.dequeue() == 1
        assert self.q.dequeue() == 2
        assert self.q.dequeue() == 3
        assert self.q.dequeue() == None

    def test_front(self):
        assert self.q.enqueue(1)
        assert self.q.enqueue(2)
        assert self.q.enqueue(3)
        assert self.q.front() == 1
        assert self.q.front() == 1
        assert self.q.dequeue() == 1
        assert self.q.front() == 2
