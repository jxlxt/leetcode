package edu.ucsc;

import java.util.Arrays;

/**
 * Leetcode Number: 561
 * Problem Name: Array Partition I
 *
 * @author: Created by Xiaotong Li 
 * @time: 6/26/18:2018-06-26 18:53.
 */
public class arrayPairSum {
    public int arrayPairSum(int[] nums) {
        Arrays.sort(nums);
        int result = 0;
        for (int i = 0; i < nums.length; i += 2) {
            result += nums[i];
        }
        return result;
    }
}
