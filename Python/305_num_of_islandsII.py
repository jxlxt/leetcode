class UnionFind:
    def __init__(self, size):
        self.num = 0
        self.parent = [i for i in range(size)]
    
    def find(self, item):
        if self.parent[item] == item:
            return item
        self.parent[item] = self.find(self.parent[item])
        return self.parent[item]
    
    def connect(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            self.parent[root_a] = root_b
            self.num -= 1
    
    def query(self):
        return self.num
    
    def set_num(self, num):
        self.num = num
        

class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        """
        m: rows
        n: cols
        """
        if n == 0 or m == 0 or not positions:
            return []
        res = []
        num_of_islands = 0 
        is_island_grid = [[False] * n for i in range(m)]
        union_find = UnionFind(m*n)
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        
        for p in positions:
            x, y = p[0], p[1]
            if not is_island_grid[x][y]:
                num_of_islands += 1
                union_find.set_num(num_of_islands)
                is_island_grid[x][y] = True
                
                for dx, dy in directions:
                    new_x = x + dx
                    new_y = y + dy
                    if self.is_valid(new_x, new_y, m, n) and is_island_grid[new_x][new_y]:
                        union_find.connect(x * n + y, new_x * n + new_y)
            num_of_islands = union_find.query()
            res.append(num_of_islands)
        return res
                    
    def is_valid(self, new_x, new_y, m, n):
        return 0 <= new_x <= m - 1 and 0 <= new_y <= n - 1
