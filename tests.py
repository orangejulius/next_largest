from nose.tools import *

from nextLargest import *

def test_insert():
    node = Node(5)
    node.insert(6)

    assert_equal(6, node.right.data)
    assert_equal(node, node.right.parent)
