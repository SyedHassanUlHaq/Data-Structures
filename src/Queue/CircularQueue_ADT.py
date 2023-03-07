class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class CircularQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            newNode.next = self.head
            newNode.prev = self.tail
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
            newNode.next = self.head
        self.size += 1

    def dequeue(self):
        if self.head is None:
            return None
        else:
            data = self.head.data
            self.head = self.head.next 
            self.head.prev = self.tail

    def rotate(self):
        if self.head is None:
            return
        else:
            self.tail = self.tail.next
            self.head = self.head.next
            self.tail.next = self.head
            self.head.prev = self.tail
