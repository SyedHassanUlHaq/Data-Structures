class Node(object):
    def __init__(self, data, next = None, previous = None, tail = None):
        self.data = data
        self.next = next
        self.previous = previous
        self.tail = tail

class DoublyLinkedList(object):
    def __init__(self, tail = None):
        self.head = None
        self.tail = tail

    def insertAtStart(self, data):
        if self.head == None:
            newNode = Node(data)
            self.head = newNode
        else:
            newNode = Node(data)
            self.head.previous = newNode
            self.head = newNode

    def insertAtEnd(self, data):
        newNode = Node(data)
        temp = self.head
        while(temp.next != None):
            temp = temp.next
        temp.next = newNode
        newNode.previous = temp

    def search(self, probe, target):
        i = 1
        val = True
        probe = self.head
        if self.head == None:
            print("List is empty")
            return False
        while probe is not None:
            if probe.data == target:
                val = True
                break
        probe = probe.next
        i = i + 1
        if val:
            print("The node is present in the list at position: ")
            print(i)
        else:
            print("The node is not present in the list")

    def delete(self, data):
        current = self.head
        while current.next is not None:
            if current.data == data:
                if current.previous is None:
                    self.head = current.next
                    current.next.previous = None
                else:
                    current.previous.next = current.next
                    current.next.previous = current.previous
                return True
            current = current.next
        return False

    def printList(self, head):
        while head is not None:
            print(head.data)
            head = head.next
