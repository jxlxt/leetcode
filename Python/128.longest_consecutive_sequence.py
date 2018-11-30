        num_set, res = set(nums), 0
        for num in nums:
            if num in num_set:
                num_set.remove(num)
                length, left, right = 1, num - 1, num + 1
                while left in num_set:
                    num_set.remove(left)
                    left -= 1 
                    length += 1
                while right in num_set:
                    num_set.remove(right)
                    right += 1
                    length += 1
                res = max(res, length)
        return res
