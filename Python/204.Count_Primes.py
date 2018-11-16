class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2: return 0
        Prime = [1] * n
        Prime[0] = Prime[1] = 0
        for i in range(2, int(n**0.5)+1):
            if Prime[i] == 1:
                Prime[i*i:n:i] = [0] * len(Prime[i*i:n:i])
        return sum(Prime)
