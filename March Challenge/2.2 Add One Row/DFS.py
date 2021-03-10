# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if not root or d <= 0 : return None
        if d == 1:
            return TreeNode(v, root, None)
        if d == 2:
            root.left = TreeNode(v, root.left, None)
            root.right = TreeNode(v, None, root.right)
        else:
            root.left == self.addOneRow(root.left, v, d - 1)
            root.right == self.addOneRow(root.right, v, d - 1)
        return root
