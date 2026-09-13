class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # n = len(grid)
        # m = len(grid[0])
        
        # def bfs(i, j):
        #     stack = deque([(i, j)])
        #     perimeter = 0
        #     grid[i][j] = -1
            
        #     while stack:
        #         i, j = stack.popleft()
        #         for (x, y) in ((1, 0), (0, 1), (0, -1), (-1, 0)):
        #             new_i = i + x
        #             new_j = j + y
        #             if 0 <= new_i < n and 0 <= new_j < m:
        #                 if grid[new_i][new_j] == 1:
        #                     stack.append((new_i, new_j))
        #                     grid[new_i][new_j] = -1
        #                 elif grid[new_i][new_j] == 0:
        #                     perimeter += 1
        #             else:
        #                 perimeter += 1
                            
        #     return perimeter
                    
        # for i in range(n):
        #     for j in range(m):
        #         if grid[i][j] == 1:
        #             return bfs(i, j)

        m, n = len(grid), len(grid[0])
        visit = set()
        def dfs(i, j):
            if (i, j) in visit:
                return 0
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == 0:
                return 1

            visit.add((i, j))
            perim = 0
            for (x, y) in ((1, 0), (0, 1), (0, -1), (-1, 0)):
                new_i = i + x
                new_j = j + y
                perim += dfs(new_i, new_j)
            return perim
            
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    return dfs(i, j)
