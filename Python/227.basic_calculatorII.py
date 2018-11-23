class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        num_ch, sign, stack, num = 0, '+', [], 0
        for ch in s:
            num_ch += 1
            if ch.isdigit():
                num = num * 10 + int(ch)
            if ch != ' ' and not ch.isdigit() or len(s) == num_ch:
                if sign == '+':
                    stack.append(num)
                if sign == '-':
                    stack.append(-num)
                if sign == '*':
                    stack.append(stack.pop()*num)
                if sign == '/':
                    stack.append(int(stack.pop()/num))
                sign = ch
                num = 0
        return sum(stack)
