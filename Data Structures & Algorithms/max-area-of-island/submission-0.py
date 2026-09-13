class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxarea = 0

        coor = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        def dfs(i, j):
            grid[i][j] = 0
            area = 1

            for x, y in coor:
                nr = i + x
                nc = j + y
                if nr in range(len(grid)) and nc in range(len(grid[0])) and grid[nr][nc] == 1:
                    area += dfs(nr, nc)

            return area
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    maxarea = max(maxarea, dfs(i, j))

        return maxarea