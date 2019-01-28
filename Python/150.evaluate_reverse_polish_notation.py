class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for t in tokens:
            if t not in ['+', '-', '*', '/']:
                stack.append(int(t))
            else:
                r, l = stack.pop(), stack.pop()
                if t == '+':
                    stack.append(l+r)
                elif t == '-':
                    stack.append(l-r)
                elif t == '*':
                    stack.append(l*r)
                else:
                    # if l*r <0 and l%r != 0:
                    #     stack.append(l//r+1)
                    # else:
                    #     stack.append(l//r)
                    stack.append(int(l * 1.0 / r))
        return stack.pop()
