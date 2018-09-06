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
    @return: the root of the minimum subtree
    """
    
    def findSubtree(self, root):
        # write your code here
        self.subtreeSum = sys.maxsize
        self.result = None
        self.helper(root)
        return self.result
    
    def helper(self, root):
        if root is None:
            return 0
            
        left_sum = self.helper(root.left)
        right_sum = self.helper(root.right)
        
        if left_sum + right_sum + root.val <= self.subtreeSum:
            self.subtreeSum = left_sum + right_sum + root.val
            self.result = root

        return left_sum + right_sum + root.val
