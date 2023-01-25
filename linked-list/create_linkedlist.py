class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node # created a head that points to new_node
        self.tail = new_node # created a tail that points to new_node
        self.lenght = 1 # gave the linked list a length of 1

my_linked_list = LinkedList(4) # assigned the value of 4 to new_node

print(my_linked_list.head.value)
# 4

'''
head ->
        4 -> None
tail -> 
'''

