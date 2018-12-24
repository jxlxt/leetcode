from collections import deque
class Solution:
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board or len(board) == 0 or len(board[0]) == 0:
            return
        m, n = len(board), len(board[0]) # m is row number, col is col number
        for i in range(m):
            self.bfs(board, i, 0)
            self.bfs(board, i, n - 1)
        for j in range(n):
            self.bfs(board, 0, j)
            self.bfs(board, m-1, j)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'W':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'

    def bfs(self, board, x, y):
        if board[x][y] != 'O':
            return
        board[x][y] = 'W'
        queue = deque()
        queue.append((x, y))
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                new_dx = x + dx
                new_dy = y + dy
                if 0 <= new_dx < len(board) and 0 <= new_dy < len(board[0]) and board[new_dx][new_dy] == 'O':
                    board[new_dx][new_dy] = 'W'
                    queue.append((new_dx, new_dy))
