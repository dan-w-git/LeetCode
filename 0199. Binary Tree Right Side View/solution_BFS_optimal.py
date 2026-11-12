# DS: Tree
# ALGO: BFS, Iteration
# Time: O(n), Space: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        q = collections.deque()
        q.append(root)

        while q:
            for i in range(len(q)):
                node = q.popleft()

                if not node:
                    continue

                if i == 0:
                    result.append(node.val)

                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)

        return result
