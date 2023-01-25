class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
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
            self.head =  new_node
            self.tail =  new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.lenght += 1
        return True


    def pop(self):
        if self.lenght == 0: # 1st if statement
            return None
        
        temp = self.head
        pre = self.head
        while (temp.next): # while temp.next is not None
            pre = temp
            temp = temp.next
        
        self.tail = pre
        self.tail.next = None
        
        self.lenght -= 1
        if self.lenght == 0: # second if statement after decrement
            self.head = None
            self.tail = None
        
        return temp # returns to the node that we just removed

my_linked_list = LinkedList(1)
my_linked_list.print_list()
# 1
my_linked_list.append(2) # 2 items
my_linked_list.print_list()
# 1
# 2
print(my_linked_list.pop()) # 2 items, returns 2 nodes
# <__main__.Node object at 0x1079cf350>
print(my_linked_list.pop()) # 1 item, returns 1 node
# <__main__.Node object at 0x107f5e1d0>
print(my_linked_list.pop()) # 0 item, returns None
# None

