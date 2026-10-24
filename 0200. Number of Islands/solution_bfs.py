# DS: Graph
# ALGO: BFS
# Time: O(m x n), Space: O(m x n)

from collections import deque
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows = len(grid)
        cols = len(grid[0])
        # store index offsets for left, right, up, down
        directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        q = deque()
        islands = 0

        for r in range(rows):
            for c in range(cols):
                # new island
                if grid[r][c] == "1":
                    q.append((r, c))
                    grid[r][c] = "0"

                    # exploring all lands of an island
                    while q:
                        row, col = q.popleft()

                        for dr, dc in directions:
                            nr, nc = row + dr, col + dc

                            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
                                q.append((nr, nc))
                                grid[nr][nc] = "0"

                    islands += 1

        return islands
