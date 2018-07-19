package edu.ucsc;

/**
 * Leetcode Number: 674
 * Problem Name: Longest Continuous Increasing Subsequence
 *
 * @author: Created by Xiaotong Li 
 * @time: 6/27/18:2018-06-27 21:44.
 */

/**
 * The idea is to use cnt to record the length of the current
 * continuous increasing subsequence which ends with nums[i],
 * and use res to record the maximum cnt.
 */
public class findLengthOfLCIS {
    public int findLengthOfLCIS(int[] nums) {
        int res = 0, cnt = 0;
        for (int i = 0; i < nums.length; i++) {
            if (i == 0 || nums[i - 1] < nums[i]) res = Math.max(res, ++cnt);
            else cnt = 1;
        }
        return res;
    }
}
