package edu.ucsc;



/**
 * Leetcode Number: 268
 * Problem Name: Missing Number
 *
 * @author: Created by Xiaotong Li 
 * @time: 6/25/18:2018-06-25 23:14.
 */
public class missingNumber {
    public int missingNumber(int[] nums) {
        int xor = 0, i = 0;
        for (i = 0; i < nums.length; i++) {
            xor = xor ^ i ^ nums[i];
        }
        return xor ^ i;
    }
}
