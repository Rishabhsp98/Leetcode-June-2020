class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        if rows == 0:
            return
        cols = len(board[0])
        for i in range(cols):
            if board[0][i] == 'O':
                self.DFS(board, 0, i)
            if board[rows-1][i] == 'O':
                self.DFS(board, rows-1, i)
        
        for i in range(rows):
            if board[i][0] == 'O':
                self.DFS(board, i, 0)
            if board[i][cols-1] == 'O':
                self.DFS(board, i, cols-1)
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == '#':
                    board[i][j] = 'O'
        return
    def DFS(self, board, i, j):
        if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or board[i][j]!='O':
            return
        
        board[i][j] = '#'
        self.DFS(board, i+1, j)
        self.DFS(board, i-1, j)
        self.DFS(board, i, j+1)
        self.DFS(board, i, j-1)
        
            
        