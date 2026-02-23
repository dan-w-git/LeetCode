# DS: Binary Tree
# ALGO: Iterative DFS
# Time: O(n). Space: O(h). h: tree height

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def dfs(node):
            nonlocal diameter

            if not node:
                return 0

            height_left = dfs(node.left)
            height_right = dfs(node.right)
            diameter = max(diameter, height_left + height_right)

            return max(height_left, height_right) + 1

        dfs(root)
        return diameter


# Object Oriented rewrite: store result variable as class attribute
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Initialize the result as an instance attribute
        self.res = 0

        # Start the recursion
        self.dfs(root)

        return self.res

    def dfs(self, node):
        if not node:
            return 0

        # Standard post-order traversal
        left = self.dfs(node.left)
        right = self.dfs(node.right)

        # Update the instance attribute directly
        self.res = max(self.res, left + right)

        # Return the height to the parent call
        return 1 + max(left, right)
