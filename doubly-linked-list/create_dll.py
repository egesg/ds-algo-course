class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None # added prev

class DoublyLinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node # created a head that points to new_node
        self.tail = new_node # created a tail that points to new_node
        self.lenght = 1 # gave the doubly linked list a length of 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

my_doubly_linked_list = DoublyLinkedList(7) # assigned the value of 7 to new_node

print(my_doubly_linked_list.head.value)
# 7
# OR
my_doubly_linked_list.print_list()
# 7

'''
head ->
        None <- 7 -> None
tail -> 
'''

