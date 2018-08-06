package edu.ucsc;

/**
 * Leetcode Number: 665
 * Problem Name: Non-decreasing Array
 *
 * @author: Created by Xiaotong Li 
 * @time: 6/27/18:2018-06-27 12:53.
 */

/**
 * the problem is like greedy problem
 */
public class checkPossibility {
    public boolean checkPossibility(int[] nums) {
        int cnt = 0; // the number of changes
        for (int i = 1; i < nums.length && cnt <= 1; i++) {
            if (nums[i - 1] > nums[i]) {
                cnt++;
                if (i - 2 < 0 || nums[i - 2] < nums[i]){
                    nums[i - 1] = nums[i]; //modify nums[i-1] of a priority
                }
                else nums[i] = nums[i - 1]; //have to modify nums[i]
            }
        }
        return cnt <= 1;
    }
}
