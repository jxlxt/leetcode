from collections import deque
class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """
    def wallsAndGates(self, rooms):
        # write your code here
        if not rooms:
            return 
        queue = deque()
        row, col = len(rooms), len(rooms[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for i in range(row):
            for j in range(col):
                if rooms[i][j] == 0:
                    queue.append((i, j))
        
        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                new_dx, new_dy = x + dx, y + dy
                if new_dx < 0 or new_dx >= row or new_dy < 0 or new_dy >= col or rooms[new_dx][new_dy] < rooms[x][y] + 1:
                    continue
                rooms[new_dx][new_dy] = rooms[x][y] + 1 
                queue.append((new_dx, new_dy))
