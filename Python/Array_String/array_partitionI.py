class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(sorted(nums)[::2])
        """
        Explaination:
        1. Assume in each pair i, bi >= ai.
        2. Denote Sm = min(a1, b1) + min(a2, b2) + ... + min(an, bn). The biggest Sm is the answer of this problem. Given 1, Sm = a1 + a2 + ... + an.
        3. Denote Sa = a1 + b1 + a2 + b2 + ... + an + bn. Sa is constant for a given input.
        4. Denote di = |ai - bi|. Given 1, di = bi - ai. Denote Sd = d1 + d2 + ... + dn.
        5. So Sa = a1 + a1 + d1 + a2 + a2 + d2 + ... + an + an + dn = 2Sm + Sd => Sm = (Sa - Sd) / 2. To get the max Sm, given Sa is constant, we need to make Sd as small as possible.
        6. So this problem becomes finding pairs in an array that makes sum of di (distance between ai and bi) as small as possible. Apparently, sum of these distances of adjacent elements is the smallest. If that's not intuitive enough, see attached picture. Case 1 has the smallest Sd.        
        """
