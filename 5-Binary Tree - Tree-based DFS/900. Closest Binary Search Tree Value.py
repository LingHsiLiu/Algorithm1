"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """
    def __init__(self):
        self.current = sys.maxsize
    
    def closestValue(self, root, target):
        # write your code here
        if root is None:
            return self.current
        if root.val == target:
            return root.value
        if abs(root.val - target) < abs(self.current - target):
            self.current = root.val
            
        if target > root.val:
            
            right = self.closestValue(root.right, target)
            if abs(right - target) < abs(self.current - target):
                return root.right
            # if abs(root.val - target) < abs(self.current - target):
            #     return root.right
        else:
            left = self.closestValue(root.left, target)
            if abs(left - target) < abs(self.current - target):
                return left
            # if abs(root.val - target) < abs(self.current - target):
            #     return root.left
        return self.current
        
