class Solution:
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix or not matrix[0]: return []
        row, col = len(matrix), len(matrix[0])
        pacific_visited = [[False for _ in range(col)] for _ in range(row)]
        atlantic_visited = [[False for _ in range(col)] for _ in range(row)]
        for i in range(row):
            self.dfs(i, 0, matrix, pacific_visited)
            self.dfs(i, col - 1, matrix, atlantic_visited)
        for j in range(col):
            self.dfs(0, j, matrix, pacific_visited)
            self.dfs(row - 1, j, matrix, atlantic_visited)
        res = []
        for i in range(row):
            for j in range(col):
                if pacific_visited[i][j] and atlantic_visited[i][j]:
                    res.append([i, j])
        return res
            
        
    def dfs(self, x, y, matrix, visited):
        visited[x][y] = True
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for dx, dy in directions:
            new_dx = x + dx
            new_dy = y + dy
            if not self.inbound(new_dx, new_dy, matrix) or visited[new_dx][new_dy] or matrix[new_dx][new_dy] < matrix[x][y]:
                continue
            self.dfs(new_dx, new_dy, matrix, visited)
    
    def inbound(self, x, y, matrix):
        if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]):
            return False
        else:
            return True
