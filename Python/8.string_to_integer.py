class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        result, n, flag, i = 0, len(str), 1, 0
        if i < n and str[0] == '+':
            i += 1
        elif i < n and str[0] == '-':
            flag = -1
            i += 1
        
        while i < n:
            if str[i].isdigit():
                if result > 214748364 or (result == 214748364 and int(str[i]) >= 8):
                    if flag == 1:
                        return 2147483647
                    else:
                        return -2147483648
                result = result * 10 + int(str[i])
                i += 1
            else:
                break
        
        return result * flag
