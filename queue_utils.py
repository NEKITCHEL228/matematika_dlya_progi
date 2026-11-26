from collections import deque

class Queue:
    def __init__(self):
        self._data = deque()
    def enqueue(self, item):
        self._data.append(item)
    def dequeue(self):
        return self._data.popleft() if self._data else None
    def is_empty(self):
        return not self._data
    def size(self):
        return len(self._data)
