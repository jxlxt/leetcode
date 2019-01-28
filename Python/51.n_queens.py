class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        if n <= 0: return 0
        res = []
        self.dfs(n, [], res)
        return res
        
    def dfs(self, n, subSet, res):
        if len(subSet) == n:
            res.append(self.draw(subSet))
        for column in range(n):
            if not self.isValid(subSet, column):
                continue
            subSet.append(column)
            self.dfs(n, subSet, res)
            subSet.pop()
    
    def draw(self, subSet):
        out = []
        for i in range(len(subSet)):
            temp = ['.'] * len(subSet)
            temp[subSet[i]] = 'Q'
            out.append(''.join(temp))
        return out
    
    def isValid(self, subSet, column):
        currentRow = len(subSet)
        for dx in range(currentRow):
            if subSet[dx] == column or abs(subSet[dx] - column) == abs(dx - currentRow):
                #这里后半部分比较其实就是用已经确定可以放置的点和将要放置的点作比较，确保斜率的绝对值为1 或者 -1
                # abs(subSet[dx] - column) == abs(dx - currentRow)
                # abs(y1-y2) == abs(x1-x2), x1, y1 表示已经确定的点的横坐标和纵坐标，x2, y2表示将要确定的那个点的横坐标和纵坐标
                return False
        return True
