# DS: 2D-Array
# ALGO: Binary Search
# Time: O(log(m*n)). Space: O(1)


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        if target < matrix[0][0] or target > matrix[m - 1][n - 1]:
            return False
        
        start = 0
        end = m * n - 1
        
        while start <= end:
            mid = (start + end) // 2
            mid_row = mid // n
            mid_col = mid % n
            mid_num = matrix[mid_row][mid_col]

            if target == mid_num:
                return True
            elif target < mid_num:
                end = mid - 1
            else:
                start = mid + 1
        
        return False