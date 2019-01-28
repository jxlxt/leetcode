class Solution:
    # time complexity: O(n)
    # space complexity: O(n)
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        digitsMap = {val: index for index, val in enumerate(str(num))}
        A = list(str(num))
        for ind, char in enumerate(str(num)):
            for digit in range(9, int(char), -1):
                d = str(digit)
                if d in digitsMap and digitsMap[d] > ind:
                    A[ind], A[digitsMap[d]] = A[digitsMap[d]], A[ind]
                    return int(''.join(map(str, A)))
        return num
