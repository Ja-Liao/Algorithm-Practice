class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        coord = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        

        def bfs(i, j):
            queue = deque([(i, j)])
            visited = set([(i, j)])
            steps = 0
            
            while queue: 
                for _ in range(len(queue)):
                    r, c = queue.popleft()

                    if grid[r][c] == 0:
                        return steps

                    for x, y in coord:
                        nr = r + x
                        nc = c + y
                        if (nr in range(len(grid)) and nc in range(len(grid[0])) 
                        and (nr, nc) not in visited and grid[nr][nc] != -1):
                            queue.append((nr, nc))
                            visited.add((nr, nc))

                steps += 1
            return 2147483647

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2147483647:
                    grid[i][j] = bfs(i, j)

        return