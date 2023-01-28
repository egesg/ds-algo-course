# depth first search - in order

class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree: # this is a method in the BST class, not a seperate function
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


    def dfs_in_order(self):
        results = []

        def traverse(curreny_node): # same recursive function with DFS pre order and post order method but results.append(curreny_node.value) line goes to middle of if statements
            if curreny_node.left is not None: 
                traverse(curreny_node.left)

            results.append(curreny_node.value)

            if curreny_node.right is not None:
                traverse(curreny_node.right)

        traverse(self.root)
        return results

my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print(my_tree.dfs_in_order()) # all of the numbers are written to list in numerical order
# [18, 21, 27, 47, 52, 76, 82]
'''
     47
    /  \
  21    76
 /  \   / \
18  27 52  82
'''
