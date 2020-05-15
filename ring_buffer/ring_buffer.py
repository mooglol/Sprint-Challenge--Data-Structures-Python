class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.index = 0

    def append(self, item):
        if len(self.storage) < self.capacity:
                self.storage.append(item)
                self.current = len(self.storage) - 1
                return

        self.current += 1
        if self.current >= self.capacity:
                self.current = 0
        self.storage[self.current] = item

    def get(self):
        return list(self.storage)