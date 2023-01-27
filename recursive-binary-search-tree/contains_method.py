# contains method
# 1. iteratilvely (look at other BST section) -> we only passed value -> (self,value)
# 2. recursively (here) -> we pass value and current_node -> (self,current_node,value)

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


    def __r_contains(self,current_node,value):
        if current_node == None: # if BST is empty
            return False
        
        if value == current_node.value: # if value I am looking for is in the tree -> return True
            return True

        if value < current_node.value:
            return self.__r_contains(current_node.left, value)
        if value > current_node.value:
            return self.__r_contains(current_node.right, value)

    def r_contains(self,value):
        return self.__r_contains(self.root, value)

my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print('BST Contains 27: ')
print(my_tree.r_contains(27))
# True

print('BST Contains 17: ')
print(my_tree.r_contains(17))
# False

