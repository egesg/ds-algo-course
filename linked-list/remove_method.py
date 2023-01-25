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
        if index < 0 or index >= self.lenght:
            return None
        
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_method(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self,index,value):
        if index < 0 or index > self.lenght:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.lenght:
            return self.append(value)

        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        
        self.lenght += 1
        return True

    
    def remove(self, index):
        if index < 0 or index >= self.lenght:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.lenght - 1:
            return self.pop()

        prev = self.get(index - 1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        
        self.lenght -= 1
        return temp # returns to the node we removed

my_linked_list = LinkedList(11)
my_linked_list.append(3)
my_linked_list.append(23)
my_linked_list.append(7)
my_linked_list.print_list()
# 11
# 3
# 23
# 7
print(my_linked_list.remove(2))
# <__main__.Node object at 0x10e0ff650>
my_linked_list.print_list()
# 11
# 3
# 7

