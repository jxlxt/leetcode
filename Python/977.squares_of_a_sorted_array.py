class Solution:
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        # time complexity: O(N)
        # space complexity: O(N)
        N = len(A)
        # seperate negative, positive part
        j = 0
        while j < N and A[j] < 0:
            j += 1
        i = j - 1
        res = []
        while 0 <= i and j < N:
            if A[i] ** 2 < A[j] ** 2:
                res.append(A[i] ** 2)
                i -= 1
            else:
                res.append(A[j] ** 2)
                j += 1
        
        while 0 <= i:
            res.append(A[i] ** 2)
            i -= 1
        while j < N:
            res.append(A[j] ** 2)
            j += 1
        return res
    
        # time complexity: O(NlogN)
        # space complexity: O(N)
        for a in range(len(A)):
            A[a] = A[a] * A[a]
        A.sort()
        return (A)
