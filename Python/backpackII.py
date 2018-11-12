class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @param V: Given n items with value V[i]
    @return: The maximum value
    """
    def backPackII(self, m, A, V):
        # write your code here
        f = [0 for _ in range(m+1)]
        n = len(A)
        for i in range(n):
            for j in range(m, A[i]-1, -1):
                f[j] = max(f[j], f[j-A[i]]+V[i])
        return f[m]

