# circular linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        if self.head is None:
            print("List is empty")
        else:
            temp = self.head
            print(temp.data, "--->", end="")
            while temp.next != self.head:
                temp = temp.next
                print(temp.data, "--->", end="")
            print(temp.data)  # Print the last node's data and a newline


L = CircularLinkedList()
n1 = Node(10)
L.head = n1 
L.tail = n1   
L.tail.next = L.head

L.display()  # Output: 10 ---> 10

n2 = Node(20)
L.tail.next = n2
L.tail = n2
L.tail.next = L.head

L.display()  # Output: 10 ---> 20   ---> 10    

n3 = Node(30)
L.tail.next = n3 
L.tail = n3
L.tail.next = L.head        

L.display()  # Output: 10 ---> 20   ---> 30   ---> 10

  