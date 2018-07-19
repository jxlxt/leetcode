package edu.ucsc;

import java.util.HashSet;
import java.util.Set;

/**
 * Leetcode Number: 217
 * Problem Name: Contains Duplicate
 *
 * @author: Created by Xiaotong Li 
 * @time: 6/25/18:2018-06-25 22:37.
 */
public class containsDuplicate {
    public boolean containDuplicate(int[] nums) {
        final Set<Integer> distinct = new HashSet<Integer>();
        for (int num: nums) {
            if (distinct.contains(num)) {
                return true;
            }
            distinct.add(num);
        }
        return false;
    }
}
