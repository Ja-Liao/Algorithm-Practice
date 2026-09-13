class Solution:
    def islandsAndTreasure(self, grid):
        rows, cols = len(grid), len(grid[0])
        q = deque()

        # Push all gates (0's) into the queue initially
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    q.append((i, j))

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        # Multi-source BFS
        while q:
            r, c = q.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                # Only update rooms (INF)
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 2147483647:
                    grid[nr][nc] = grid[r][c] + 1
                    q.append((nr, nc))
