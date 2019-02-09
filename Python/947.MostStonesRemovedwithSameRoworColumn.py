#! /Users/xiaotongli/anaconda3/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2/4/19 6:59 PM
# @Author  : Xiaotong Li
# @School  : University of California, Santa Cruz
# @FileName: 947.MostStonesRemovedwithSameRoworColumn.py
# @Software: PyCharm
import collections
class Solution:
    import collections
    class Solution:
        def removeStones(self, stones):
            """
            :type stones: List[List[int]]
            :rtype: int
            """

            #         index = collections.defaultdict(set)
            #         for i, j in stones:
            #             index[i].add(j + 10000)
            #             index[j+10000].add(i)

            #         def dfs(i):
            #             seen.add(i)
            #             for j in index[i]:
            #                 if j not in seen:
            #                     dfs(j)

            #         islands = 0
            #         seen = set()
            #         for i, j in stones:
            #             if i not in seen:
            #                 islands += 1
            #                 dfs(i)
            #                 dfs(j + 10000)
            #         return len(stones) - islands
            def find(x):
                if x != parents[x]:
                    parents[x] = find(parents[x])
                return parents[x]

            def union(x, y):
                parents[find(x)] = find(y)

            parents = list(range(20001))
            for i, j in stones:
                union(i, j + 10000)
            return len(stones) - len({find(x) for x, y in stones})



if __name__ == '__main__':
    sol = Solution()
    stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
    print(sol.removeStones(stones))


