class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numsRows == 1 or numsRows >= len(s):
            return s

        L = ['']*numRows
        index, step = 0, 1
        for word in s:
            L[index] += word
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step

        return ''.join(L)
