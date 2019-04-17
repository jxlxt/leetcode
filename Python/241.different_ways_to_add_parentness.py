class Solution:
    def diffWaysToCompute(self, inputs: str) -> List[int]:
        # divide and conquer
        if inputs.isdigit():
            return [int(inputs)]
        res = []
        for i in range(len(inputs)):
            if inputs[i] in "+-*":
                res1 = self.diffWaysToCompute(inputs[:i])
                res2 = self.diffWaysToCompute(inputs[i+1:])
                for j in res1:
                    for k in res2:
                        res.append(self.helper(j, k, inputs[i]))
        return res
    
    def helper(self, m, n, ops):
        if ops == '+':
            return m + n
        elif ops == '-':
            return m - n
        elif ops == '*':
            return m * n
