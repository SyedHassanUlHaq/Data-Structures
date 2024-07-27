class Node :
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Bag:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        cur = Node(data)
        if self.head == None:
            self.head = cur
            self.tail = cur
        else:
            self.tail.next = cur
            self.tail = cur

    def prepend(self, data):
        cur = Node(data)
        cur.next = self.head
        self.head = cur

    def insert(self, index, data):
        cur = Node(data)
        if index == 0:
            cur.Next = self.head
            self.head = cur
        else:
            prev = self.head
            for i in range(index - 1):
                prev = prev.next
            cur.next = prev.next
            prev.next = cur
    
    def delete(self, index):
        if index == 0:
            self.head = self.head.next
        else:
            prev = self.head
            for i in range(index - 1):
                prev = prev.next
            prev.next = prev.next.next

    def traverse(self):
        cur = self.head
        while cur != None:
            print(cur.data, end="")
            cur = cur.next
        print()

    def removeAll(self, head):
        if head == None:
            return None
        else:
            cur = head
            while cur != None:
                prev = cur 
                cur = cur.next
                prev.next = None
            return cur
        
    def __iter__(self):
        return _BagIterator(self.head)

class _BagIterator:
    def __init__(self, head):
        self.cur = head

    def __next__(self):
        if self.cur == None:
            raise StopIteration
        else:
            data = self.cur.data
            self.cur = self.cur.next
            return data