class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # the first solution is newton method
        # to determine whether it is a perfect square, actually we determin
        # function x^2 = n, which get the answer x. For newton method, we
        # change the function as x^2 - n = 0, we get the x' = x - (x^2 - n)/2x
        # based on the newton method theory, which also can be written as
        # x' = 1/2 * (x + n/x)
        r = num
        while r*r > num:
            r = (r + num//r) // 2
        return r*r == num

        # the second method is binary search
        low, high = 1, num
        while low <= high:
            mid = low + (high - low) // 2
            buffer = num // mid
            if buffer < mid:
                high = mid - 1
            elif buffer > mid:
                low = mid + 1
            elif (num%mid == 0):
                return True
            else:
                return False
        return False
