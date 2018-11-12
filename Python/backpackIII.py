class Solution:
    """
    @param A: an integer array
    @param V: an integer array
    @param m: An integer
    @return: an array
    """
    def backPackIII(self, A, V, m):
        # write your code here
        f = [0 for _ in range(m+1)]
        for (a, v) in zip(A, V):
            for j in range(a, m+1):
                if f[j-a] + v > f[j]:
                    f[j] = f[j - a] + v 
        return f[m]
