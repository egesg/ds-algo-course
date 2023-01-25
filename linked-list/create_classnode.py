class LinkedList:
    def __init__(self,value): # creates a new node and initializes the "NewLinkList"
        pass

    def append(self, value): # creates a new node and adds that node to "end"
        pass

    def prepend(self,value): # creates a new node and adds that node to "beginning"
        pass

    def insert(self, index, value): # creates a new node and inserts thay node at given index
        pass

# this class does nothing but creates nodes
# when any of these 4 methods needs to create a new node, they will call on the class Node
class Node:
    def __init__(self, value): # contains only constructer
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,value): # constructer
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.lenght = 1

