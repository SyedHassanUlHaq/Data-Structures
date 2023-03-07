class Node :
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None

    def traverse(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def remove(self, data):
        current = self.head
        if current.data  == data:
            self.head = current.next
            return True
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return True
            current = current.next
        return False

    def append(self, data):
        current = self.head 
        while current.next:
            current = current.next
        current.next = Node(data)

    def removeAll(self):
        current = self.head
        count = 0 
        while current:
            count += 1
            current = current.next
        mid = count // 2
        print("mid", mid)
        current = self.head
        for i in range(mid - 1):
            current = current.next
        new_list = LinkedList()
        new_list.head = current.next
        current.next = None
        return new_list

    def split_in_half(self):
        current = self.head
        count = 0
        while current:
            count+=1
            current = current.next
        mid = count // 2 
        print ("mid", mid)
        current = self.head
        for i in range(mid - 1):
            current = current.next
        new_list = LinkedList()
        new_list.head = current.next
        current.next = None
        return new_list

