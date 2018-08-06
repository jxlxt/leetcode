package edu.ucsc;

import java.util.HashMap;
import java.util.Map;

/**
 * Leetcode Number: 532
 * Problem Name: K-diff Pairs in an Array
 *
 * @author: Created by Xiaotong Li 
 * @time: 6/26/18:2018-06-26 12:59.
 */
public class findPairs {
    public int findPairs(int[] nums, int k) {
        if (nums == null || nums.length == 0 || k < 0) return 0;
        Map<Integer, Integer> map = new HashMap<Integer, Integer>();
        int count = 0;
        for (int i : nums) {
//            map.put(i, map.getOrDefault(i, 0) + 1);
        }
        for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
            if (k == 0) {
                if (entry.getValue() >= 2) {
                    count++;
                }
            }else {
                if (map.containsKey(entry.getKey() + k)) {
                    count++;
                }
            }
        }
        return count;
    }
}
