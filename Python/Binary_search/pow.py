class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """

        if n == 0:
            return 1
        if n < 0:
            n = -n
            x = 1/x
        # pow() is a built in function in python3
        # it will return the value of x^y
        if n%2 == 0:
            return pow(x*x, n//2)
        else:
            return pow(x*x, n//2) *x
