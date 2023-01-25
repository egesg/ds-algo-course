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
        if self.lenght == 0:
            return None
        
        temp = self.head
        pre = self.head
        while (temp.next):
            pre = temp
            temp = temp.next
        
        self.tail = pre
        self.tail.next = None
        
        self.lenght -= 1
        if self.lenght == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self,value):
        new_node = Node(value)
        if self.lenght == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.lenght += 1
        return True

    def pop_first(self):
        if self.lenght == 0:
            return None

        temp = self.head
        self.head = self.head.next
        temp.next = None
        
        self.lenght -= 1
        if self.lenght == 0:
            self.tail = None
        return temp


    def get(self,index):
        if index < 0 or index >= self.lenght: # test if index is valid (not negative)
            return None
        
        temp = self.head
        for _ in range(index):
            temp = temp.next
        
        return temp

my_linked_list = LinkedList(0)
my_linked_list.append(1)
my_linked_list.append(3)
my_linked_list.append(3)
my_linked_list.print_list()
# 0
# 1
# 2
# 3
print(my_linked_list.get(2))
# <__main__.Node object at 0x104dc3010>

