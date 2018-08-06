package edu.ucsc;

import java.util.HashSet;
import java.util.Set;

/**
 * Leetcode Number: 219
 * Problem Name: Contains Duplicate II
 *
 * @author: Created by Xiaotong Li 
 * @time: 6/25/18:2018-06-25 22:58.
 */
public class containsNearbyDuplicate {
    public  boolean containsNearbyDuplicate(int[] nums, int k) {
        Set<Integer> set = new HashSet<Integer>();
        for (int i = 0; i < nums.length; i++) {
            if (i > k) set.remove(nums[i - k - 1]);
            if (!set.add(nums[i])) return true;
        }
        return false;
    }
}
