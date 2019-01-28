class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """  
        def solve_partial_sudoku(i, j):
            # row by row, col by col
            if i == len(board):
                i = 0
                j += 1 
                # if col number equal to the final return, finish searching
                if j == len(board[i]):
                    return True
            # pruning, skip nonempty entrys
            if board[i][j] != empty_entry:
                return solve_partial_sudoku(i+1, j)
            
            def valid_to_sudoku(i, j, val): 
                # check row 
                if any(val == board[k][j] for k in range(len(board))):
                    return False
                # check col
                if val in board[i]:
                    return False
                # check region
                boxrow = i - i%3
                boxcol = j - j%3
                return not any(val == board[i][j] for i in range(boxrow, boxrow+3) for j in range(boxcol, boxcol+3))
            
            for val in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                if valid_to_sudoku(i, j, val):
                    board[i][j] = val
                    if solve_partial_sudoku(i+1, j):
                        return True
            board[i][j] = empty_entry
            return False        
        empty_entry = '.'
        solve_partial_sudoku(0, 0)
