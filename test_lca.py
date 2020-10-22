import unittest
import LowCA

class Testlca(unittest.TestCase):

    def test_findLCA(self):

        root = LowCA.Node(1)
        result = LowCA.findLCA(root, 4, 5)
        self.assertEquals(-1, -1) #only root in tree
        root.left = LowCA.Node(2)
        root.right = LowCA.Node(3)
        root.left.left = LowCA.Node(4)
        root.left.right = LowCA.Node(5)
        root.right.left = LowCA.Node(6)
        root.right.right = LowCA.Node(7)
        result = LowCA.findLCA(root, 4, 5)
        self.assertEquals(2, result)
