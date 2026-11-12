# DS: Tree
# ALGO: DFS
# Time: O(n^2). Space: O(h)
# Time O(n²) worst case for a skewed tree, and O(n log n) for a balanced one
# Space: at any moment the stack holds at most: d (isValidBST frames) + (h - d) (helper frames) ≈ h

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def subtreeMin(node):
            if not node:
                return float("inf")
            return min(node.val, subtreeMin(node.left), subtreeMin(node.right))

        def subtreeMax(node):
            if not node:
                return float("-inf")
            return max(node.val, subtreeMax(node.left), subtreeMax(node.right))

        if subtreeMax(root.left) >= root.val or subtreeMin(root.right) <= root.val or not self.isValidBST(root.left) or not self.isValidBST(root.right):
            return False

        return True
