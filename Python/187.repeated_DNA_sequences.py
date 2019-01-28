class Solution:
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        dictionary = {}
        for i in range(len(s) - 9):
            key = s[i:i+10]
            if key not in dictionary:
                dictionary[key] = 1
            else:
                dictionary[key] += 1
        res = []
        for val in dictionary:
            if dictionary[val] > 1:
                res.append(val)
        return res
