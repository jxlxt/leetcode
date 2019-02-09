import collections
class Solution:
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        d = collections.defaultdict(int)
        for s in A:
            even = ''.join(sorted(s[0::2]))
            odd = ''.join(sorted(s[1::2]))
            d[(even, odd)] += 1
        return len(d)
        
