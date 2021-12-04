class LinkedList:
    class Node:
        def __init__(self, value=None):
            self.value = value
            self.next = None

    def __init__(self):
        self.first = LinkedList.Node()
        self.last = LinkedList.Node()
        self.size = 0

    def isEmpty(self) -> bool:
        return self.first.value is None

    def addLast(self, item: int):
        node = LinkedList.Node(item)
        if self.isEmpty():
            self.first = self.last = node
        else:
            self.last.next = node
            self.last = node

        self.size += 1
        return node

    def addFirst(self, item):
        node = linkedlist.Node(item)

        if self.isEmpty():
            self.first = self.last = node
        else:
            node.next = self.first
            self.first = node

        self.size += 1

    def indexOf(self, item: int):
        index = 0
        current = self.first

        while current is not None:
            if current.value == item:
                return index
            current = current.next
            index = index + 1

        return -1

    def contains(self, item: int) -> bool:
        return self.indexOf(item) is not -1

    def removeFirst(self):
        if self.isEmpty():
            raise BaseException

        if self.first == self.last:
            self.first = self.last = None
        else:
            second = self.first.next
            self.first.next = None
            self.first = second

        self.size -= 1

    def removeLast(self):
        if self.isEmpty():
            raise BaseException

        if self.first == self.last:
            self.first = self.last = None

        else:
            previous = self.getPrevious(self.last)
            self.last = previous
            self.last.next = None

        self.size -= 1

    def getPrevious(self, node):
        current = self.first
        while current is not None:
            if current.next == node:
                return current
            current = current.next

        return None

    def toArray(self):
        array = [None] * self.size
        current = self.first
        index = 0
        while current is not None:
            array[index] = current.value
            current = current.next
            index = index + 1
            
        return array

    def reverse(self):
        if self.isEmpty():
            return None
        previous = self.first
        current = self.first.next
        while current is not None:
            next = current.next
            current.next = previous
            previous = current
            current = next

        self.last = self.first
        self.last.next = None
        self.first = previous


if __name__ == "__main__":
    linkedlist = LinkedList()
    linkedlist.addLast(10)
    linkedlist.addLast(20)
    linkedlist.addLast(30)
    linkedlist.addLast(40)
    linkedlist.addFirst(100)
    print(linkedlist.indexOf(10))
    print(linkedlist.contains(40))
    linkedlist.removeFirst()
    linkedlist.removeLast()
    linkedlist.reverse()
    print(linkedlist.toArray())
    print(linkedlist)
