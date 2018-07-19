package edu.ucsc;

/**
 * Leetcode Number: 27
 * Problem Name: Remove Element
 *
 * @author: Created by Xiaotong Li 
 * @time: 6/20/18:2018-06-20 23:02.
 */
public class removeElement {
    public int removeElement(int[] nums, int val) {
        if (nums.length == 0) return 0;
        int i = 0;
        for (int j = 0; j < nums.length; j++) {
            if (nums[j] != val) {
                nums[i] = nums[j];
                i++;
            }
        }
        return i;
    }
}
