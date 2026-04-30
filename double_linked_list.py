class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def display(self):
        if self.head is None:
            print("Double Linked List is empty")
            return
        else:
            temp = self.head
            while temp:
                 print(temp.data,"-->", end=" ")
                 temp = temp.next

    def insert_beginning(self, data):
        n = Node(data)
        temp = self.head
        temp.prev = n
        n.next = temp
        self.head = n

    def insert_end(self, data):
        n = Node(data)
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = n   
        n.prev = temp

    def inser_position(self,data, pos):
        n = Node(data)
        temp = self.head
        for i in range(pos-1):
            temp = temp.next
        n.prev = temp
        n.next = temp.next
        temp.next.prev = n
        temp.next = n

    def insert_after(self, data, pos):
        n = Node(data)
        temp = self.head
        for i in range(pos-1):
            temp = temp.next
        n.prev = temp
        n.next = temp.next
        if temp.next is not None:
            temp.next.prev = n
        temp.next = n    

    def insert_before(self, data, pos):
        n = Node(data)
        temp = self.head
        for i in range(pos-1):
            temp = temp.next
        n.next = temp
        n.prev = temp.prev
        if temp.prev is not None:
            temp.prev.next = n
        else:
            self.head = n
        temp.prev = n   

    def delete_beginning(self):
        temp = self.head
        self.head = temp.next
        temp.next = None
        self.head.prev = None    

    def delete_end(self):
        temp = self.head
        before = self.head
        while temp.next is not None:
            temp = temp.next
            before = before.next
        before.next = None
        temp.prev = None    

    def delete_position(self, pos):
        temp =self.head
        before = self.head
        for i in range(1,pos-1):  
            temp = temp.next
            before = before.next 
        before.next = temp.next
        temp.next.prev = before
        temp.next = None
        temp.prev = None 
  
L = DoubleLinkedList()
L.head = Node(10)
second = Node(20)
third = Node(30)            
L.head.next = second
second.prev = L.head
second.next = third
third.prev = second 
third.next = None
L.tail = third  


L.insert_beginning(5)
L.insert_end(15) 
L.inser_position(25, 3) 
L.insert_after(35, 4)
L.insert_before(12, 5)
L.delete_beginning()
L.delete_position(5)
L.delete_end()
L.display()