import unittest
import LowCA

class TestLowCA(unittest.TestCase):

    def test_findLCA(self):

        root = lowCA.Node(1)
        result = lowCA.findLCA(root, 4, 5)
        self.assertEquals(2, -1) #only root in tree
        root.left = lowCA.Node(2)
        root.right = lowCA.Node(3)
        root.left.left = lowCA.Node(4)
        root.left.right = lowCA.Node(5)
        root.right.left = lowCA.Node(6)
        root.right.right = lowCA.Node(7)
        result = lowCA.findLCA(root, 4, 5)
        self.assertEquals(2, result)
