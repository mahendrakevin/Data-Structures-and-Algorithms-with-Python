class Queue:
    def __init__(self, length):
        self.items: list = [None] * length
        self.rear: int = 0
        self.front: int = 0
        self.count: int = 0

    def enqueue(self, item):
        if self.isFull():
            raise ValueError('Full')
        self.items[self.rear] = item
        self.rear = (self.rear + 1) % len(self.items)
        self.count += 1

    def dequeue(self):
        if self.isEmpty():
            raise ValueError('Queue is empty')
        item = self.items[self.rear]
        self.items[self.front] = 0
        self.front = (self.front + 1) % len(self.items)
        self.count -= 1

        return item

    def peek(self):
        if self.isEmpty():
            raise ValueError

        return self.items[self.front]

    def reverse(self):
        if self.isEmpty():
            raise ValueError

        reversed_queue = []
        for i in range(len(self.items) - 1, -1, -1):
            reversed_queue.append(self.items[i])
        return reversed_queue

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == len(self.items)

    def toArray(self):
        return self.items


queue = Queue(length=5)

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.enqueue(50)
queue.dequeue()
queue.dequeue()
queue.enqueue(60)
queue.enqueue(70)
print(queue.dequeue())
queue.enqueue(80)
print(queue.toArray())


