package edu.ucsc;

import java.util.HashMap;

/**
 * Leetcode Number: 594
 * Problem Name: Longest Harmonious Subsequence
 *
 * @author: Created by Xiaotong Li 
 * @time: 7/3/18:2018-07-03 21:29.
 */
public class findLHS {
    public int findLHS(int[] nums) {
        HashMap<Long, Integer> map = new HashMap<Long, Integer>();
//        for (long num: nums) {
//            map.put(num, map.getOrDefault(num, 0) + 1);
//        }
        int result = 0;
        for (long key: map.keySet()) {
            if (map.containsKey(key + 1)) {
                result = Math.max(result, map.get(key + 1) + map.get(key));
            }
        }
        return result;
    }
}
