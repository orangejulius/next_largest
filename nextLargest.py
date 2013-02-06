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

# find the next largest node in a binary tree
#
# there are two places to look for the next largest node: the right
# subtree and the ancestors. the left subtree contains only nodes
# smaller than the curernt node, so it doesn't have to be considered
#
# an ancestor node COULD be the next largest, but only if the current node
# is in its left subtree (the ancestor node is larger)
# however such an ancestor would also have all the current node's descendents
# as its own decendends, meaning it is larger than all of them, and thus not
# the NEXT largest
#
# so, return the smallest node in the right subtree if it exists, otherwise
# return the next largest ancestor
def nextLargest(node):
    minInRightSubtree = minInSubtree(node.right)
    smallestLargerAncestor = getSmallestLargerAncestor(node)
    if minInRightSubtree:
        return minInRightSubtree.data
    elif smallestLargerAncestor:
        return smallestLargerAncestor.data
    else:
        return None

# the smallest node in a subtree can be found by traversing
# left as long as possible
def minInSubtree(node):
    if not node:
        return None
    while node.left:
        node = node.left
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
