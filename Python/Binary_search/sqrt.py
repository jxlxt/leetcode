class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """ 
        """
        The first method: Binary Search
        set two pointer left and right, if we find the x is between mid^2 and
        (mid+1)^2 becasue the return is int sqrt(int x)
        """
        if x == 0:
            return 0
        left, right = 0, x
        while left <= right:
            mid = left + (left + right) // 2
            if mid * mid <= x < (mid+1)*(mid+1):
                return mid
            elif: mid * mid < x:
                left = mid + 1
            else: 
                right = mid - 1

        """
        The second method: Newton Method
        """
        r = x
        while r * r > x:
            r = (r + x / r) // 2
        return int(r)
