class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            mem = set()
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    continue
                if board[i][j] not in mem:
                    mem.add(board[i][j])
                else:
                    return False
        
        for j in range(len(board[0])):
            mem = set()
            for i in range(len(board)):
                if board[i][j] == '.':
                    continue
                if board[i][j] not in mem:
                    mem.add(board[i][j])
                else:
                    return False

        for k in range(0, len(board), 3):
            for q in range(0, len(board[0]), 3):
                mem = set()
                for i in range(k, k + 3):
                    for j in range(q, q + 3):
                        if board[i][j] == '.':
                            continue
                        if board[i][j] not in mem:
                            mem.add(board[i][j])
                        else:
                            return False

        return True