"""
Stack implemented using two queues.

This module assumes a Queue class with: enqueue(int), dequeue()->int,
front()->int, is_empty()->bool, clear()->None.
"""

from __future__ import annotations
from queue import Queue

class StackFromQueues:
    """
    A LIFO stack implemented using two FIFO queues.

    At any time, **exactly one** of q1 or q2 holds all the elements; the other is empty.
    Push appends to the non-empty queue.
    Top/Pop shift elements to expose/remove the most-recently-pushed value.
    """

    def __init__(self) -> None:
        self.q1 = Queue()
        self.q2 = Queue()

    def is_empty(self) -> bool:
        """Return True iff both queues are empty."""
        return self.q1.is_empty() and self.q2.is_empty()

    def _active_and_passive(self):
        """
        Helper: return (active, passive) where active is the non‑empty queue.
        If both are empty, treat q1 as active and q2 as passive.
        """
        if not self.q1.is_empty():
            return self.q1, self.q2
        else:
            return self.q2, self.q1

    def push(self, value: int) -> None:
        """
        Enqueue into whichever queue is currently non‑empty.
        If both are empty, enqueue into q1.
        """
        active, _ = self._active_and_passive()
        active.enqueue(value)

    def top(self) -> int:
        """
        Return the top value *without removing* it.

        Raises:
            AssertionError if the stack is empty.
        """
        assert not self.is_empty(), "top() called on empty stack"
        active, passive = self._active_and_passive()
        # Move all elements except the last one to the passive queue
        last = None
        while not active.is_empty():
            val = active.dequeue()
            if active.is_empty():
                last = val
            else:
                passive.enqueue(val)
        # Enqueue the last element to passive to preserve the stack contents
        if last is not None:
            passive.enqueue(last)
        return last

    def pop(self) -> int:
        """
        Remove and return the top value.

        Raises:
            AssertionError if the stack is empty.
        """
        assert not self.is_empty(), "pop() called on empty stack"
        active, passive = self._active_and_passive()
        # Move all elements except the last one to the passive queue
        last = None
        while not active.is_empty():
            val = active.dequeue()
            if active.is_empty():
                last = val
            else:
                passive.enqueue(val)
        # Do NOT enqueue the last element – it is removed
        return last

    def clear(self) -> None:
        """Clear both queues to free memory."""
        self.q1.clear()
        self.q2.clear()
    
