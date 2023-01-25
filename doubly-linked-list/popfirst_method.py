class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.lenght = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        self.lenght += 1
        return True

    def pop(self):
        if self.lenght == 0:
            return None

        temp = self.tail
        if self.lenght == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        
        self.lenght -= 1
        return temp

    def prepend(self,value):
        new_node = Node(value)

        if self.lenght == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        
        self.lenght += 1
        return True


    def pop_first(self):
        if self.lenght == 0: # if there is no item
            return None
        
        temp = self.head
        if self.lenght == 1: # if there is only 1 item
            self.head = None
            self.tail = None
        else: # if there are 2 or more items
            self.head = self.head.next
            self.head.prev = None
            temp.next = None

        self.lenght -= 1
        return temp

my_doubly_linked_list = DoublyLinkedList(2)
my_doubly_linked_list.append(1)
my_doubly_linked_list.print_list()
# 2
# 1
print(my_doubly_linked_list.pop_first()) # 2 items -> returns to 2 nodes
# <__main__.Node object at 0x107cb2c90>
print(my_doubly_linked_list.pop_first()) # 1 item -> returns to 1 node
# <__main__.Node object at 0x107746b90>
print(my_doubly_linked_list.pop_first()) # 0 item -> returns to None
# None

