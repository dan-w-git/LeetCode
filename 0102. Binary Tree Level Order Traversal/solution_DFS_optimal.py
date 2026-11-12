# DS: Tree
# ALGO: DFS, Recursion
# Time: O(n). Space: O(h)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []

        def dfs(node: Optional[TreeNode], depth: int):
            if not node:
                return None

            if len(result) == depth:
                result.append([])

            result[depth].append(node.val)
            dfs(node.left, depth+1)
            dfs(node.right, depth+1)

        dfs(root, 0)
        return result
