class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if len(num1) == 0 or len(num2) == 0:
            return "0"
        digits, product, sum_ = [0] * (len(num2) + len(num1)), 0, 0
        for i in reversed(range(len(num1))):
            for j in reversed(range(len(num2))):
                p1, p2 = i + j, i + j + 1
                product = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                sum_ = product + digits[p2]
                digits[p1] += sum_ // 10
                digits[p2] = sum_ % 10
        res = []
        for digit in digits:
            if not (len(res) == 0 and digit == 0):
                res.append(digit)
        return [''.join(map(str, res)), "0"][len(res) == 0]
#        Explaination
#        1 2 3
#        * 4 5
#        -----
#          1 5
#        1 0
#      0 5
#        1 2
#      0 8
#    0 4
#    ----------
#ind 0 1 2 3 4 5 
#   <-----------
#length is lenght(num1) + length(num2)
#indices[p1, p2]  p1 = i + j, p2 = i + j + 1 for i and j is the index number of
#num1 and num2
