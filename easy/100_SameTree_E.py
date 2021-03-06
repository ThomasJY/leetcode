# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
           
        if p is None and q is None:
            return True
        else:
            if p is not None and q is not None:
                if p.val != q.val:
                    return False
                else:
                    return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)     
            else:
                return False
