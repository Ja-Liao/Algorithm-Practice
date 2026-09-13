class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        res = 0
        coord = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        fresh = 0
        q = collections.deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    q.append((i, j))

        while fresh > 0 and q:
            length = len(q)
            
            for i in range(length):
                r, c = q.popleft()
                for x, y in coord:
                    nr = x + r
                    nc = y + c
                    if nr in range(len(grid)) and nc in range(len(grid[0])) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append((nr, nc))
                        fresh -= 1

            res += 1

        return res if fresh == 0 else -1


