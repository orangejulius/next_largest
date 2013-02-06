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
