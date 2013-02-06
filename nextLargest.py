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
    minInRightSubtree = minInSubtree(node.right)
    if minInRightSubtree and not node.parent:
        return minInRightSubtree.data
    elif node.parent and not node.right:
        return node.parent.data
    else:
        return min(node.parent.data, minInRightSubtree.data)

def minInSubtree(node):
    if node and node.left:
        return minInSubtree(node.left)
    else:
        return node

#the smallest larger ancestor is the first ancestor whos child enroute to the node
#is the left side child
def getSmallestLargerAncestor(node):
    #traverse along all ancestors who have the current node as right side child
    while node.parent and node.parent.right == node:
        node = node.parent
    #return parent if this node is the right side child. otherwise no ancestor is larger
    if node.parent and node.parent.left == node:
        return node.parent
