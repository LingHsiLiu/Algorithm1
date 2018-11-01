"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the maximum average of subtree
    """
    # average, node = 0, None
    
    def findSubtree2(self, root):
        # Write your code here

        sum, size, node, average = self.helper(root)
        return node

    def helper(self, root):
        if root is None:
            return 0, 0, root, 0

        left_sum, left_size, left_Node, left_average = self.helper(root.left)
        right_sum, right_size, right_Node, right_average = self.helper(root.right)

        sum, size = left_sum + right_sum + root.val, left_size + right_size + 1
        
        if left_average > right_average:
            if left_Node is None or sum * 1.0 / size > left_average:
                node = root
                average = sum * 1.0 / size
            else:
                node = left_Node
                average = left_average
        else:
            if right_Node is None or sum * 1.0 / size > right_average:
                node = root
                average = sum * 1.0 / size
            else:
                node = right_Node
                average = right_average

        return sum, size, node, average
        
