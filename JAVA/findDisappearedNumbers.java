package edu.ucsc;

import java.util.ArrayList;
import java.util.List;

/**
 * Leetcode Number: 448
 * Problem Name: Find All Numbers Disappeared in an Array
 *
 * @author: Created by Xiaotong Li 
 * @time: 6/26/18:2018-06-26 09:05.
 */
public class findDisappearedNumbers {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        List<Integer> ret = new ArrayList<Integer>();
        for (int i = 0; i < nums.length; i++) {
            int val = Math.abs(nums[i]) - 1;
            if (nums[val] > 0) {
                nums[val] = - nums[val];
            }
        }

        for (int i = 0; i < nums.length; i++) {
            if (nums[i] > 0) {
                ret.add(i + 1);
            }
        }
        return ret;
    }
}
