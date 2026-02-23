# DS: Binary Tree
# ALGO: BFS / Iterative DFS
# Time: O(n). Space: O(n), d: max tree depth

"""
BFS: use deque (FIFO)
Iterative DFS: use stack (LIFO)
"""

from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        stack = [root]

        while stack:
            node = stack.pop()
            node.left, node.right = node.right, node.left

            if node.left:
                stack.append(node.left)

            if node.right:
                stack.append(node.right)

        return root
