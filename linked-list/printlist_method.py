class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

    def print_list(self): # not a built-in method
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.lenght = 1

my_linked_list = LinkedList(4)

