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
    @param k: the given k
    @return: the kth smallest element in BST
    """
    def kthSmallest(self, root, k):
        # write your code here
        
        stack = []
        while root:
            stack.append(root)
            root = root.left
            print(root)
            
        for i in range(k - 1):
            if not stack:
                break
            if stack[-1].right:
                node = stack[-1].right
                print(node)
                while node:
                    stack.append(node)
                    node = node.left

            else:
                node = stack.pop()
                while stack and stack[-1].right == node:
                    node = stack.pop()
                
        return stack[-1].val
        
