# DS: Binary Tree
# ALGO: Iterative DFS
# Time: O(n). Space: O(n)
"""
Using stack (LIFO), right sub-tree is explored to the leaf before colapsing each level and backing up max depth
"""

from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth = 0
        stack = [(root, 1)]
        while stack:
            node, depth = stack.pop()
            depth += 1  # depth of child nodes if present

            if node.left:
                stack.append((node.left, depth))
                max_depth = max(max_depth, depth)
            if node.right:
                stack.append((node.right, depth))
                max_depth = max(max_depth, depth)

        return max_depth

# equivalent


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = [(root, 1)]
        res = 0

        while stack:
            node, depth = stack.pop()

            if node:
                res = max(res, depth)
                stack.append((node.left, depth + 1))
                stack.append((node.right, depth + 1))
        return res
