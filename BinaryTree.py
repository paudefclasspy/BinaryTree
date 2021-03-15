class Node:
    def __init__(self,value =None):
        self.value = value
        self.left_child = None
        self.right_child = None
class BST:
    def __init__(self):
        self.root = None # Head

    def insert(self,value):
        if self.root==None:
            self.root = Node(value)
        else:
            self._insert(value,self.root)
    def _insert(self,value,cur_node):
        if value<cur_node.value:
            if cur_node.left_child==None:
                cur_node.left_child=Node(value)
            else:
                self._insert(value, cur_node.left_child)
        elif value>cur_node.value:
            if cur_node.right_child==None:
                cur_node.right_child=Node(value)
            else:
                self._insert(value, cur_node.right_child)
        else:
            print("Already in the Tree!")
    def print_tree(self):
        if self.root!=None:
            self._print_tree(self.root)
    def _print_tree(self, cur_node):
        if cur_node!=None:
            self._print_tree(cur_node.left_child)
            print(str(cur_node.value))
            self._print_tree(cur_node.right_child)
def fill_tree(tree,elems = 100, max = 1000):
    from random import randint
    for _ in range(elems):
        cur_elem = randint(0,max)
        tree.insert(cur_elem)
    return tree
tree = BST()
tree = fill_tree(tree)
tree.print_tree()