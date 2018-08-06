package edu.ucsc;

/**
 * Leetcode Number: 53
 * Problem Name: Maximum Sub-array
 *
 * @author: Created by Xiaotong Li 
 * @time: 6/20/18:2018-06-20 23:22.
 */
public class maxSubArray {
    public int maxSubArray(int[] nums) {
        int res = nums[0];
        int sum = nums[0];
        for (int i = 1; i < nums.length; i++) {
            sum = Math.max(nums[i], sum + nums[i]);
            res = Math.max(res, sum);
        }
        return res;
    }
}
