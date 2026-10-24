# DS: Array
# ALGO:
# Time: O(n * h). Space: O(n * h)

class Solution:
    def trap(self, height: List[int]) -> int:
        # base case
        n = len(height)
        if n == 1:
            return 0

        # iterate height list once to store height as keys and list of indices with each height as values into a dict
        height_dict = {}
        for i in range(n):
            point_height = height[i]
            # index at every height up to max height of a point
            while point_height > 0:
                height_dict.setdefault(point_height, []).append(i)
                point_height -= 1

        # calculate water row by row using two pointers
        water = 0
        for point_height, index_list in height_dict.items():
            if len(index_list) == 1:
                continue

            for i in range(len(index_list) - 1):
                left = index_list[i]
                right = index_list[i+1]
                water += right - left - 1

        return water
