# DS: Binary Tree
# ALGO: Recursive DFS
# Time: O(n). Space: O(h)

# Space:
# Best case (balanced tree): O(log(n))
# Worst case (degenerate tree): O(n)

from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
