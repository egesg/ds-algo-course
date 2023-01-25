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
        if self.lenght == 0: # 1st if statement 
            return None

        temp = self.head
        self.head = self.head.next
        temp.next = None
        
        self.lenght -= 1
        if self.lenght == 0: # 2nd if statement after decrement
            self.tail = None

        return temp # item we just removed (returns to the entire node)


my_linked_list = LinkedList(2)
my_linked_list.append(1)
my_linked_list.print_list()
# 2
# 1
print(my_linked_list.pop_first()) # 2 items, returns 2 nodes
# <__main__.Node object at 0x110ff9010>
print(my_linked_list.pop_first()) # 1 item, returns 1 node
# <__main__.Node object at 0x111005610>
print(my_linked_list.pop_first()) # 0 item, returns None
# None

