package edu.ucsc;

/**
 * Leetcode Number: 643
 * Problem Name: Maximum Average Subarray I
 *
 * @author: Created by Xiaotong Li 
 * @time: 6/27/18:2018-06-27 09:03.
 */

/**
 * sliding window
 */
public class findMaxAverage {
    public double findMaxAverage(int[] nums, int k) {
        long sum = 0;
        for (int i = 0; i < k; i++) sum += nums[i];
        long max = sum;

        for (int i = k; i < nums.length; i++) {
            sum += nums[i] - nums[i - k];
            max = Math.max(max, sum);
        }
        return max/1.0/k;
    }
}
