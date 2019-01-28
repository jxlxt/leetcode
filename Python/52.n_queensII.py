class Solution:
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        """
        Python 里面函数参数是引用类型，也就是对象。所以你直接放一个数字进去python会把数字作为按值传递处理，返回的时候参数永远不会被函数内部改变，
        假如你把那个ans = 0 放进一个只有一个元素list的或者嵌入到一个新对象传就没事。
        """
        if n <= 0: return 0
        self.ans = 0
        self.dfs(n, [])
        return self.ans
        
    def dfs(self, n, subSet):
        if len(subSet) == n:
            self.ans += 1
        for column in range(n):
            if not self.isValid(subSet, column):
                continue
            subSet.append(column)
            self.dfs(n, subSet)
            subSet.pop()
            
    def isValid(self, subSet, column):
        currentRow = len(subSet)
        for dx in range(currentRow):
            if subSet[dx] == column or abs(dx - currentRow) == abs(subSet[dx] - column):
                return False
        return True
