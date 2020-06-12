

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = []
        self.curr = 0
    def append(self, item):
        if len(self.queue)is self.capacity:
            self.queue[self.curr] = 0
            self.queue[self.curr] = item
            self.curr = (self.curr + 1) % self.capacity
        else:
            self.queue.append(item)

    def get(self):
        return self.queue

b = RingBuffer(5)
b.append('a')
b.append('b')
b.append('c')
b.append('d')
b.append('e')
b.append('f')
print(b.get())