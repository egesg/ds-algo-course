# 1st part:
# start from the root -> traverse it -> find the node you wanna delete -> if you cannot find, return None

# 2nd part:
# 1- is it a leaf node? (simplest scenario)
# 2- is it a node that has a subtree on the left or right? (move the subtree up to the place of the node you are deleting)
# 3- is it a node that has subtrees on the both sides? (find the lowest value of the right subtree, copy that node value into the place of the node you are deleting, remove the lowest value of right subtree)

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
        if current_node == None:
            return False
        
        if value == current_node.value:
            return True

        if value < current_node.value:
            return self.__r_contains(current_node.left, value)
        if value > current_node.value:
            return self.__r_contains(current_node.right, value)

    def r_contains(self,value):
        return self.__r_contains(self.root, value)

    def __r_insert(self,current_node,value):
        if current_node == None:
            return Node(value) # returns to None(value)
        
        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)
        if value > current_node.value:
            current_node.right = self.__r_insert(current_node.right, value)
        return current_node

    def r_insert(self, value):
        if self.root == None: 
            self.root = Node(value)
        self.__r_insert(self.root, value)


    # create helper method
    def min_value(self, current_node): # find the min value of the subtree
        while current_node.left is not None: # to find the min value of subtree, it has to be always open (None) on the left side
            current_node = current_node.left # so, if it is not open (None), it keeps going to the left side
        return current_node.value # not returning to the node, returning to the value of the node

    def __delete_node(self,current_node,value):
        if current_node == None: # if value that i wanna delete is not in the BST
            return None # similar to the recursive insert method but I return None instead of returning to Node(value). once it returns to None, it gets popped from the call stack.

        if value < current_node.value: # traverse to the left
            current_node.left = self.__delete_node(current_node.left, value)
        elif value > current_node.value: # traverse to the right
            current_node.right = self.__delete_node(current_node.right, value)
        else: # it covers 4 situations 1-deleting a leaf node 
              #                        2-node that has opening on the left but a node on the right 
              #                        3-node that has opening on the right but a node on the left
              #                        4-node that has node on each sides ( find the min value of the subtree first)
            if current_node.left == None and current_node.right == None: # 1-if it is a leaf node
                return None # so it gets popped from the call stack
            elif current_node.left == None: # 2-node that has opening on the left but has a node on the right 
                current_node = current_node.right
            elif current_node.right == None: # 3-node that has opening on the right but has a node on the left
                current_node = current_node.left
            else: # 4-node that has node on both left and right sides
                sub_tree_min = self.min_value(current_node.right) # find the min value of right substree
                current_node.value = sub_tree_min # copy the min value of subtree to current node
                current_node.right = self.__delete_node(current_node.right, sub_tree_min) # (this line and line 86 is almost identical) remove the min value of right subtree from the tree
        return current_node

    def delete_node(self,value):
        self.__delete_node(self.root, value)

# to test min_value helper method only
my_tree_test = BinarySearchTree()
my_tree_test.insert(47)
my_tree_test.insert(21)
my_tree_test.insert(76)
my_tree_test.insert(18)
my_tree_test.insert(27)
my_tree_test.insert(52)
my_tree_test.insert(82)

print(my_tree_test.min_value(my_tree_test.root))
# 18
print(my_tree_test.min_value(my_tree_test.root.right))
# 52

# to test the entire delete_node method
my_tree = BinarySearchTree()
my_tree.insert(2)
my_tree.insert(1)
my_tree.insert(3)
'''
CREATES THIS TREE
    2
   / \
  1   3
'''
print('root:', my_tree.root.value)
# root: 2
print('root.left:', my_tree.root.left.value)
# root.left: 1
print('root.right:', my_tree.root.right.value)
# root.right: 3

my_tree.delete_node(2)
'''
EXPECTING THIS TREE
    3
   / \
  1   None
'''
print('root:',my_tree.root.value)
# root: 3
print('root.left:',my_tree.root.left.value)
# root.left: 1
print('root.right:',my_tree.root.right)
# root.right: None

