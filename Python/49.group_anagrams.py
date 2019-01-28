from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = defaultdict(list)
        for string in strs:
            dic[''.join(sorted(string))] += [string]

        return [value for key, value in dic.items()]
