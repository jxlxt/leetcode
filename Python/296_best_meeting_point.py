class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        rows, cols = [], []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    rows.append(i)
                    cols.append(j)
        # rows dont need sort becasue when we append row index, it has already sorted
        cols = sorted(cols)
        res, i, j = 0, 0, len(rows)-1
        while i < j:
            res += rows[j] - rows[i] + cols[j] - cols[i]
            j -= 1
            i += 1
        return res
