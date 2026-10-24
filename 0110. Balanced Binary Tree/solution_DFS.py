# DS: Binary Tree
# ALGO: DFS
# Time: O(n). Space: O(h)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        height_balanced = True

        def treeDepth(node):
            nonlocal height_balanced

            if not node:
                return 0

            depth_left = treeDepth(node.left)
            depth_right = treeDepth(node.right)
            if abs(depth_left - depth_right) > 1:
                height_balanced = False

            return max(depth_left, depth_right) + 1

        treeDepth(root)
        return height_balanced
