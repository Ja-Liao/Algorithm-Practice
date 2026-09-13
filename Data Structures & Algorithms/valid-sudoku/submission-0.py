class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()

        for i in range(len(board)):
            for j in range(len(board[0])):
                val = board[i][j]
                if val == '.':
                    continue
                r = ('r', i, val)
                c = ('c', j, val)
                
                box_id = ("b", i // 3, j // 3, val)
                # if any already present -> invalid
                if r in seen or c in seen or box_id in seen:
                    return False
                seen.add(r)
                seen.add(c)
                seen.add(box_id)
        return True