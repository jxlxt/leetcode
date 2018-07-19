package edu.ucsc;

/**
 * Leetcode Number: 136
 * Problem Name: Single Number
 *
 * @author: Created by Xiaotong Li 
 * @time: 6/29/18:2018-06-29 09:03.
 */

/**
 * using XOR method
 */
public class singleNumber {
    public int singleNumber(int[] nums) {
        int n = nums.length, result = 0;
        for (int i = 0; i < n; i++) result = result^nums[i];
        return result;
    }
}
