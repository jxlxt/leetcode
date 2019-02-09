class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # traverse the graph
        # count the neighbour
        if grid is None: return 0
        area, connect = 0, 0
        row, col = len(grid), len(grid[0])
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    area += 1
                    if r < row - 1 and grid[r+1][c] == 1:
                        connect += 1
                    if c < col - 1 and grid[r][c+1] == 1:
                        connect += 1
        return area*4 - connect*2
