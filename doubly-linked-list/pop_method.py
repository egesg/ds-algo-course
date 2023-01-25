# it is simpler than linked list since there is .prev

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
        if self.lenght == 0: # if doubly linked list is empty
            return None
        
        temp = self.tail
        self.tail = self.tail.prev
        self.next = None # (self.tail.next = None ?)
        temp.prev = None
        
        self.lenght -= 1
        if self.lenght == 0: # if there is only 1 node
            self.head = None
            self.tail = None
        
        return temp

my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.print_list()
# 1
# 2
print(my_doubly_linked_list.pop()) # 2 items -> returns 2 nodes
# <__main__.Node object at 0x10191ead0>
print(my_doubly_linked_list.pop()) # 1 item -> returns 1 node
# <__main__.Node object at 0x101e8a090>
print(my_doubly_linked_list.pop()) # 0 item -> return to None
# None

