from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        square = defaultdict(set)

        # iが行でjが列
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                
                if board[i][j] in row[i]:
                    return False
                else:
                    row[i].add(board[i][j])

                if board[i][j] in col[j]:
                    return False
                else:
                    col[j].add(board[i][j])

                if board[i][j] in square[i // 3, j // 3]:
                    return False

                square[i // 3, j // 3].add(board[i][j])
        return True


