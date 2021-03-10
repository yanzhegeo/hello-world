class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        
        if d == 1:
            new_node = TreeNode(v)
            new_node.left = root
            return new_node
        
        stack = []
        stack.append((root,1))
        while len(stack):
            node, depth = stack.pop(0)
            
            if (depth+1) == d:
                new_node = TreeNode(v)
                new_node.left = node.left
                node.left = new_node
                new_node = TreeNode(v)
                new_node.right = node.right
                node.right = new_node

            else:
                if node.left: stack.append((node.left, depth+1))
                if node.right: stack.append((node.right, depth+1))
        
        return root
