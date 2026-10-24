# DS: Binary Tree
# ALGO: Iterative DFS
# Time: O(n). Space: O(n)
"""
Using deque (FIFO), each level is explored from left to right before moving to the next level
"""

from typing import Optional
from collections import deque

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        q = deque()
        if root:
            q.append(root)
        level = 0

        while q:
            # only process nodes in current level (existing nodes in queue). increment level when all nodes in current level are processed
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1

        return level
