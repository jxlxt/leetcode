class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # res = []
        # if not nums or len(nums) == 0:
        #     return res
        # countA, countB = 0, 0
        # candidateA, candidateB = nums[0], nums[0]
        # for num in nums:
        #     if num == candidateA:
        #         countA += 1
        #         continue
        #     if num == candidateB:
        #         countB += 1
        #         continue
        #     if countA == 0:
        #         candidateA = num
        #         countA += 1
        #         continue
        #     if countB == 0:
        #         candidateB = num
        #         countB += 1
        #         continue
        #     countA -= 1
        #     countB -= 1
        # countA, countB = 0, 0
        # for num in nums:
        #     if num == candidateA:
        #         countA += 1
        #     elif num == candidateB:
        #         countB += 1
        # if countA > len(nums)//3:
        #     res.append(candidateA)
        # if countB > len(nums)//3:
        #     res.append(candidateB)
        # return res
        if not nums:
            return []
        cand1, cand2, count1, count2 = 0, 1, 0, 0
        for n in nums:
            if n == cand1:
                count1 += 1
            elif n == cand2:
                count2 += 1
            elif count1 == 0:
                cand1, count1 = n, 1
            elif count2 == 0:
                cand2, count2 = n, 1
            else:
                count1 -= 1
                count2 -= 1
        return [n for n in [cand1, cand2] if nums.count(n) > len(nums) // 3]
