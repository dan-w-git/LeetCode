# DS: Tree
# ALGO: BFS
# Time: O(n). Space: O(n)
# For a balanced tree, h ≈ log n but the width is ≈ n/2, so BFS is O(n) while DFS is O(log n).
# For a skewed tree (a linked list), h = n but width = 1, so BFS is O(1) there and DFS is O(n).
# Worst case across all trees, BFS is O(n).


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        # q = collections.deque((root, float("-inf")))
        q = collections.deque()
        q.append((root, float("-inf")))

        while q:
            node, max_val = q.popleft()

            if not node:
                continue

            if node.val >= max_val:
                res += 1
                max_val = node.val

            if node.left:
                q.append((node.left, max_val))
            if node.right:
                q.append((node.right, max_val))

        return res
