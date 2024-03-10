from typing import Any


class BufferList:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = []

    def is_empty(self) -> bool:
        return len(self.buffer) == 0

    def is_full(self) -> bool:
        return len(self.buffer) == self.capacity

    def enqueue(self, item) -> None:
        if self.is_full():
            print("Buffer is full")
        self.buffer.append(item)

    def dequeue(self) -> Any:
        if self.is_empty():
            raise IndexError("Buffer is empty")
        return self.buffer.pop(0)


class BufferRing:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = [None] * capacity
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self) -> bool:
        return self.size == 0

    def is_full(self) -> bool:
        return self.size == self.capacity

    def enqueue(self, item) -> None:
        if self.is_full():
            print("Buffer is full")
        if self.is_empty():
            self.buffer[self.head] = item
        else:
            self.head = (self.head + 1) % self.capacity
            self.buffer[self.head] = item
        self.size += 1

    def dequeue(self) -> Any:
        if self.is_empty():
            raise IndexError("Buffer is empty")
        item = self.buffer[self.tail]
        self.tail = (self.tail + 1) % self.capacity
        self.size -= 1
        return item

