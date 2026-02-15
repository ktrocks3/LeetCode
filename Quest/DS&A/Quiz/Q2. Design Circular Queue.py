class MyCircularQueue:

    def __init__(self, k: int):
        self.data = [0] * k
        self.head = 0
        self.count = 0
        self.size = k

    def enQueue(self, value: int) -> bool:
        if self.count >= self.size:
            return False
        tail = (self.head + self.count) % self.size
        self.data[tail] = value
        self.count += 1
        return True

    def deQueue(self) -> bool:
        if self.count == 0:
            return False
        self.head = (self.head + 1) % self.size
        self.count -= 1
        return True

    def Front(self) -> int:
        if self.count == 0:
            return -1
        return self.data[self.head]

    def Rear(self) -> int:
        if self.count == 0:
            return -1
        tail = (self.head + self.count - 1) % self.size
        return self.data[tail]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.size == self.count


# Your MyCircularQueue object will be instantiated and called as such:
k = 1
value = 1
obj = MyCircularQueue(k)
param_1 = obj.enQueue(value)
param_2 = obj.deQueue()
param_3 = obj.Front()
param_4 = obj.Rear()
param_5 = obj.isEmpty()
param_6 = obj.isFull()
