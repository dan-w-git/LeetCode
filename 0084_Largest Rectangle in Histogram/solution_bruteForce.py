# DS: Array
# ALGO:
# Time: O(n^2). Space: O(1)

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # brute force
        # iterate over array; check each width configurations to the left of current bar
        max_area = heights[0]

        for i in range(1, len(heights)):
            max_area = max(heights[i] * 1, max_area)
            shortest = heights[i]

            for j in range(i - 1, -1, -1):
                shortest = min(heights[j], shortest)
                area_i_to_j = (i - j + 1) * shortest
                max_area = max(area_i_to_j, max_area)

        return max_area
