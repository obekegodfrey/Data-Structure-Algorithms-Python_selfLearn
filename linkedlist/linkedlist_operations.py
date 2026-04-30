class Node:
    def __init__(self, data):
        self.data = data
        self.next = None #Address of Next Node

class SingleLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node  

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node  

    def insert_after_node(self, prev_node_data, data):
        new_node = Node(data)
        temp = self.head
        while temp and temp.data != prev_node_data:
            temp = temp.next
        if temp is None:
            print("Previous node not found.")
            return
        new_node.next = temp.next
        temp.next = new_node  

    def insert_before_node(self, next_node_data, data):
        new_node = Node(data)
        if self.head is None:
            print("Linked List is empty.")
            return
        if self.head.data == next_node_data:
            new_node.next = self.head
            self.head = new_node
            return
        temp = self.head
        while temp.next and temp.next.data != next_node_data:
            temp = temp.next
        if temp.next is None:
            print("Next node not found.")
            return
        new_node.next = temp.next
        temp.next = new_node

    def insert_at_position(self, position, data):    
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        temp = self.head
        for i in range(position - 1):
            temp = temp.next
            if temp is None:
                print("Position out of bounds.")
                return
        new_node.next = temp.next
        temp.next = new_node
         
    def delete_at_beginning(self):
        if self.head is None:
            print("Linked List is empty.")
            return
        temp = self.head
        self.head = temp.next
        temp = None    

    def delete_node(self, key):
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
        if temp is None:
            print("Node not found.")
            return
        prev.next = temp.next
        temp = None

    def delete_node_at_position(self, position):
        if self.head is None:
            print("Linked List is empty.")
            return
        temp = self.head
        if position == 0:
            self.head = temp.next
            temp = None
            return
        for i in range(position - 1):
            temp = temp.next
            if temp is None:
                print("Position out of bounds.")
                return
        if temp is None or temp.next is None:
            print("Position out of bounds.")
            return
        next_node = temp.next.next
        temp.next = None
        temp.next = next_node

    def display(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            temp = self.head
            while temp:
                print(temp.data,"-->",end=" ")
                temp = temp.next

L = SingleLinkedList()
n = Node(10)
L.head = n
n1 = Node(20)
L.head.next = n1
n2 = Node(30)
n1.next = n2
n3 = Node(40)
n2.next = n3

L.insert_at_beginning(5)
L.insert_at_end(50)
L.display()