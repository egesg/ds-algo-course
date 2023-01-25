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

    # dont repeat the code
    def pop(self):
        if self.lenght == 0: # if doubly linked list is empty
            return None

        temp = self.tail
        if self.lenght == 1: # if there is only 1 node
            self.head = None
            self.tail = None
        else: # if there are 2 or more nodes
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        
        self.lenght -= 1
        return temp

my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.print_list()
# 1
# 2
print(my_doubly_linked_list.pop()) # 2 items -> returns 2 nodes
# <__main__.Node object at 0x1023668d0>
print(my_doubly_linked_list.pop()) # 1 item -> returns 1 node
# <__main__.Node object at 0x102366850>
print(my_doubly_linked_list.pop()) # 0 item -> return to None
# None

