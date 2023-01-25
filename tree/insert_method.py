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
        
        if self.root is None: # if tree is empty, new node will be root
            self.root = new_node
            return True
        temp = self.root # if tree is not empty, temp will be root

        while(True):
            if new_node.value == temp.value: # there cannot be duplicates
                return False
            
            if new_node.value < temp.value: # if it is less than -> go LEFT
                if temp.left is None: # if the spot is open
                    temp.left = new_node
                    return True
                temp = temp.left # spot is not open so we move
            else: # if it is greater than -> go RIGHT
                if temp.right is None: # if the spot is empty
                    temp.right = new_node
                    return True
                temp = temp.right # if there is an item there

my_tree = BinarySearchTree()
print(my_tree)
# <__main__.BinarySearchTree object at 0x10d0e4850>

my_tree.insert(2) # I added first item with insert method, not at the same time that I created the tree
my_tree.insert(1)
my_tree.insert(3)

print(my_tree.root.value)
# 2
print(my_tree.root.left.value)
# 1
print(my_tree.root.right.value)
# 3

