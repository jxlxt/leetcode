class Solution:
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        red, green, blue = 0, 0, 0
        for cr, cb, cg in costs:
            red, blue, green = min(blue, green) + cr, min(red, green) + cb, min(red, blue) + cg
        return min(red, green, blue)


if __name__=='__main__':
    costs = [[17,2,17],[16,16,5],[14,3,19]]
    sol = Solution()
    print(sol.minCost(costs))
