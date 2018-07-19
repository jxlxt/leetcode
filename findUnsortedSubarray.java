package edu.ucsc;

/**
 * Leetcode Number: 581
 * Problem Name: Shortest Unsorted Continuous Subarray
 *
 * @author: Created by Xiaotong Li 
 * @time: 6/26/18:2018-06-26 22:59.
 */
public class findUnsortedSubarray {
    public int findUnsortedSubarray(int[] nums) {
        int n = nums.length, beg = -1, end = -2, min = nums[n - 1], max = nums[0];
        for (int i = 1; i < n; i++) {
            max = Math.max(max, nums[i]);
            min = Math.min(min, nums[n - 1 - i]);
            if (nums[i] < max) end = i;
            if (nums[n - 1 - i] > min) beg = n - 1 - i;
        }
        return end - beg + 1;
    }
}
