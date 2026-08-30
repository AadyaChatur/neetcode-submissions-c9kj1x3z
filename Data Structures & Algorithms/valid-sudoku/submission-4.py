class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(len(board)):
            seen = set()
            for j in range(len(board)):
                if board[i][j] == '.':
                    continue
                
                if board[i][j] in seen:
                    return False
                
                seen.add(board[i][j])
        

        for i in range(len(board)):
            seen = set()
            for j in range(len(board)):
                if board[j][i] == '.':
                    continue
                
                if board[j][i] in seen:
                    return False
                
                seen.add(board[j][i])

        for i in range(0,9,3):
            for j in range(0,9,3):
                seen = set()
                for row in range(0,3):
                    for col in range(0,3):
                        if board[i+row][j+col] == '.':
                            continue
                        
                        if board[i+row][j+col] in seen:
                            return False
                        
                        seen.add(board[row+i][col+j])

        return True
