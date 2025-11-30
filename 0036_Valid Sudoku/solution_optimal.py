# DS: 2-D Array, Set
# ALGO:
# Time: O(n^2). Space: O(n^2). n is length of board.

from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # store numbers appearing in each row into a separate set; store 9 sets into a list
        # store numbers appearing in each column into a separate set; store 9 sets into a list
        # store numbers appearing in each 3x3 box into a separate set; store 9 sets into a list
        n = 9
        boxes = int(n / 3)
        row_list = [set() for i in range(n)]
        col_list = [set() for i in range(n)]
        box_list = [[set() for j in range(boxes)] for i in range(boxes)]

        # iterate over the board to fill sets to check validity
        for row in range(n):
            for col in range(n):
                num = board[row][col]
                if num == ".":
                    continue
                box_set = box_list[row//3][col//3]
                if num in row_list[row] or num in col_list[col] or num in box_set:
                    return False
                row_list[row].add(num)
                col_list[col].add(num)
                box_set.add(num)

        return True
