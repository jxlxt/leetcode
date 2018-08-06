package edu.ucsc;

/**
 * Leetcode Number: 724
 * Problem Name: Find Pivot Index
 *
 * @author: Created by Xiaotong Li 
 * @time: 6/27/18:2018-06-27 22:08.
 */
public class pivotIndex {
    public int pivotIndex(int[] nums) {
        int sum = 0, left = 0;
        for (int i = 0; i < nums.length; i++) sum += nums[i];
        for (int i = 0; i < nums.length; i++) {
            if (i != 0) left += nums[i - 1];
            if (sum - left - nums[i] == left) return i;
        }
        return -1;
    }
}
