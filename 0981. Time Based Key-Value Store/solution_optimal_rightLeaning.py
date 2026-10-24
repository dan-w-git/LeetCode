# DS: Array
# ALGO: Binary Search. Boundary Search. Maximize Search
# Time: O(logn). Space: O(n). n: number of set calls

class TimeMap:

    def __init__(self):
        # initialize dict with key as dict key and list of (timestamp, value) tuples as dict value
        self.timeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key] = self.timeMap.get(key, [])
        self.timeMap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        # binary search to find max timestamp up to specified timestamp
        if key not in self.timeMap:
            return ""
        values = self.timeMap[key]
        left = 0
        right = len(values) - 1

        if timestamp < values[0][0]:
            return ""

        while left < right:
            mid = (left + right + 1) // 2
            if values[mid][0] <= timestamp:
                # mid within right boundary. try to go right to maximize. keep mid as potential answer
                left = mid
            else:
                # mid outside right boundary. go left. discard mid
                right = mid - 1
        return values[left][1]

# [1, 5, 10, 20]
# timestamp = 15
# left = 0 (1)
# right = 3 (20)
# mid = 2 (10)
# timestamp > values[mid]
# left = 2 (10)

# mid = 3 (20)
# timestamp < values[mid] (15 < 20)
# right = 2 (10)
# return 10 (<15)
