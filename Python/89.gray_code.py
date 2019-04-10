class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = []
        # G(i) = i ^ (i/2)
        for i in range(pow(2, n)):
            res.append((i>>1)^i)
        return res
