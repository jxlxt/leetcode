#! /Users/xiaotongli/anaconda3/bin/python
# -*- coding: utf-8 -*-
# @Time    : 9/28/18 10:57 PM
# @Author  : Xiaotong Li
# @School  : University of California, Santa Cruz
# @FileName: autocomplete_System.py
# @Software: PyCharm

class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # this method use set
        p = set()
        for num in nums:
            if num in p:
                return num
            else:
                p.add(num)

        # this method use two pointer
        # fast and slow pointer
        p1, p2 = nums[0], nums[0]
        while True:
            p1 = nums[p1]
            p2 = nums[nums[p2]]
            if p1 == p2:
                break
        p1 = nums[0]
        while p1 != p2:
            p1 = nums[p1]
            p2 = nums[p2]
        return p2

        # this method use binary search
        low, high = 1, len(nums) - 1

        while low < high:
            mid = low + (high - low) // 2
            count = 0
            for i in nums:
                if i <= mid:
                    count += 1
            if count <= mid:
                low = mid + 1
            else:
                high = mid
        return low
