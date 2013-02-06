class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = self.parent = 0

    def insert(self, data):
        if data < self.data:
            if self.left:
                self.left.insert(data)
            else:
                self.left = Node(data)
                self.left.parent = self
        else:
            if self.right:
                self.right.insert(data)
            else:
                self.right = Node(data)
                self.right.parent = self

def nextLargest(node):
    return min(node.parent.data, node.right.data)
