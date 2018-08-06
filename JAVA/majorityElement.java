package edu.ucsc;

/**
 * Leetcode Number: 169
 * Problem Name: Majority Element
 *
 * @author: Created by Xiaotong Li 
 * @time: 6/25/18:2018-06-25 08:56.
 */
public class majorityElement {
    public int majorityElement(int[] nums) {
        int major = nums[0], count = 1;
        for (int i = 0; i < nums.length; i++) {
            if (count == 0) {
                count++;
                major = nums[i];
            }else if (major == nums[i]) {
                count++;
            }else  count--;
        }
        return major;
    }
}
