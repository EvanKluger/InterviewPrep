class Node:
        def __init__(self, data):
            self.data = data
            self.right = None
            self.left = None

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        if self.root == None:
            self.root = Node(data)
        else:
            self.insert_recursive(self.root, data)
    
    def insert_recursive(self, node, data):
        if data <= node.data:
            if node.left == None:
                node.left = data
                return
            else:
                self.insert_recursive(node.left, data)
        else:

            if node.right == None:
                node.right = data
                return
            else:
                self.insert_recursive(node.right, data)    
    def is_empty(self):
        return self.root == None

    def search(self, data):
        if self.is_empty() == True:
            return None
        
        search_node = self.root
        
        while search_node:
            if search_node.data == data:
                return search_node.data
            if data < search_node.data:
                search_node = search_node.left
            if data > search_node.data:
                search_node = search_node.right

        return None
    

        
    

