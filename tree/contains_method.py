class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True

        temp = self.root

        while(True):
            if new_node.value == temp.value:
                return False
            
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right


    def contains(self,value): # look up by value
        '''
        if self.root is None:
            return False
        '''
        
        temp = self.root # temp = None
        while temp is not None:
            if value < temp.value: # value is less than -> go LEFT
                temp = temp.left
            elif value > temp.value: # value is greater than -> go RIGHT
                temp = temp.right
            else: # value is equal to -> return True
                return True
        return False # value is not in the tree -> return False

my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)
print(my_tree.root.value)
# 47
print(my_tree.contains(27))
# True
print(my_tree.contains(17))
# False

