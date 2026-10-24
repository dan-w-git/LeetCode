# DS: 2-D Array, Set
# ALGO:
# Time: O(n^2). Space: O(n^2). n is length of board.

from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # A single hash map to store all seen numbers with their location/constraint
        # The key format is: (constraint_type, index, number)
        # Example keys: ('row', 0, '5'), ('col', 4, '3'), ('box', (1, 2), '8')
        seen = set()
        n = 9

        for r in range(n):
            for c in range(n):
                num = board[r][c]

                if num != ".":
                    box_key = (r // 3, c // 3)
                    if ('row', r, num) in seen or ('col', c, num) in seen or ('box', box_key, num) in seen:
                        return False
                    seen.add(('row', r, num))
                    seen.add(('col', c, num))
                    seen.add(('box', box_key, num))

        return True
