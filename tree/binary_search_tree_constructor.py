class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    '''
        def __init__(self,value) -> None: 
        new_node = Node(value) # when I pass the value it creates the first node
        self.root = new_node
    '''
    # contructor of BST
    def __init__(self) -> None: # here I create empty tree
        self.root = None # it returns to None

my_tree = BinarySearchTree()

print(my_tree.root)
# None

