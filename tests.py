from nose.tools import *

from nextLargest import *

def test_insert():
    node = Node(5)
    node.insert(6)

    assert_equal(6, node.right.data)
    assert_equal(node, node.right.parent)

def test_one_child_one_parent():
    node = Node(6)
    node.insert(3)
    node.insert(5)

    assert_equal(5, nextLargest(node.left))

def test_one_parent():
    """
    No child this time, so null values must be considered
    """
    node = Node(6)
    node.insert(3)

    assert_equal(6, nextLargest(node.left))

def test_one_child():
    """
    No child this time, so null values must be considered
    """
    node = Node(6)
    node.insert(7)

    assert_equal(7, nextLargest(node))

def test_answer_is_subchild():
    """
    The next largest value is not a direct ancestor or descendent
    """
    node = Node(7)
    node.insert(3)
    node.insert(5)
    node.insert(4)

    assert_equal(4, nextLargest(node.left))

def test_minInSubtree():
    node = Node(5)
    node.insert(4)

    assert_equal(node.left, minInSubtree(node))

def test_answer_is_grandparent():
    node = Node(7) #      7
    node.insert(4) #     /
    node.insert(6) #    4
                   #     \
                   #      6 <-

    assert_equal(7, nextLargest(node.left.right))
