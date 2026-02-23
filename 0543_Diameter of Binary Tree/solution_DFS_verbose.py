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
        height, diameter = self.dfs(root)
        return diameter

    def dfs(self, node):
        if not node:
            return 0, 0
        
        height_left, diameter_left = self.dfs(node.left)
        height_right, diameter_right = self.dfs(node.right)
        height = max(height_left, height_right) + 1
        diameter = max(diameter_left, diameter_right, height_left + height_right)

        return height, diameter