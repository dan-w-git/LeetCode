# DS: 2D-Array
# ALGO: Binary Search
# Time: O(log(m*n)). Space: O(1)


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        if target < matrix[0][0] or target > matrix[m - 1][n - 1]:
            return False

        start_row = 0
        end_row = m - 1
        while start_row <= end_row:
            mid_row = (start_row + end_row) // 2
            first_num_mid_row = matrix[mid_row][0]
            last_num_mid_row = matrix[mid_row][-1]
            if target == first_num_mid_row:
                return True
            elif target < first_num_mid_row:
                end_row = mid_row - 1
            elif target > first_num_mid_row and target <= last_num_mid_row:
                # target within range of mid row
                break
            else:  # target > matrix[mid_row][-1]
                start_row = mid_row + 1

        start_col = 0
        end_col = n - 1
        while start_col <= end_col:
            mid_col = (start_col + end_col) // 2
            mid_num = matrix[mid_row][mid_col]
            if target == mid_num:
                return True
            elif target < mid_num:
                end_col = mid_col - 1
            else:
                start_col = mid_col + 1

        return False
