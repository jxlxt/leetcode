class Solution:
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        length, Increase, Decrease = len(A), False, False
        if n<=2: return True
        for i in range(1, length):
            if A[i - 1] > A[i]:
                isGreat = True
            if A[i - 1] < A[i]:
                isLess = True

            if isGreat and isLess:
                return False

        return True
