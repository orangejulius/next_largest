class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = self.parent = None

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
    if node.right and not node.parent:
        return node.right.data
    elif node.parent and not node.right:
        return node.parent.data
    else:
        return min(node.parent.data, node.right.data)

def minInSubtree(node):
    if node and node.left:
        return minInSubtree(node.left)
    else:
        return node
