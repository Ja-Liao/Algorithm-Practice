class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])

        direction = [[0, 1], [1, 0], [-1, 0], [0, -1]]

        def dfs(i, j):
            if 0 <= i < rows and 0 <= j < cols and board[i][j] == 'O':
                board[i][j] = 'T'
            else:
                return

            for x, y in direction:
                nr = i + x
                nc = j + y
                dfs(nr, nc)

        for i in range(rows):
            if board[i][0] == 'O':
                dfs(i, 0)
            if board[i][cols - 1] == 'O':
                dfs(i, cols - 1)
        
        for j in range(cols):
            if board[0][j] == 'O':
                dfs(0, j)
            if board[rows - 1][j] == 'O':
                dfs(rows - 1, j)

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    board[i][j] = 'X'

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'T':
                    board[i][j] = 'O'

        return