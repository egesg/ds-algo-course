# insert method
# 1. iteratilvely (look at other BST section) -> we only passed value -> (self,value)
# 2. recursively (here) -> we pass value and current_node -> (self,current_node,value)

# recursive contain method -> has return statement
# recursive insert method  -> does not have return statement

class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:

    def __init__(self) -> None:
        self.root = None

    def __r_contains(self,current_node,value):
        if current_node == None:
            return False
        
        if value == current_node.value:
            return True

        if value < current_node.value:
            return self.__r_contains(current_node.left, value)
        if value > current_node.value:
            return self.__r_contains(current_node.right, value)

    def r_contains(self,value): # this has return statement different than r_insert
        return self.__r_contains(self.root, value)


    def __r_insert(self,current_node,value):
        if current_node == None: # creates a new node
            return Node(value) # returns to that node
        
        if value < current_node.value: # traverse to the left
            current_node.left = self.__r_insert(current_node.left, value)
        if value > current_node.value: # traverse to the right
            current_node.right = self.__r_insert(current_node.right, value)

        return current_node # if I insert a value which is equal to the current_node.value -> returns to current_node and goes to r_insert() method. (There cannot be duplicates in the tree)

    def r_insert(self, value): # does not have return statement
        if self.root == None: # if BST is emtpy 
            self.root = Node(value) # returns to the new node that we are inserting
        self.__r_insert(self.root, value)

my_tree = BinarySearchTree()
my_tree.r_insert(2)
my_tree.r_insert(1)
my_tree.r_insert(3)
'''
BST WILL LOOK LIKE THIS
    2
   / \
  1   3
'''
print('Root:', my_tree.root.value)
# Root: 2
print('Root -> Left:', my_tree.root.left.value)
# Root -> Left: 1
print('Root -> Right:', my_tree.root.right.value)
# Root -> Right: 3

