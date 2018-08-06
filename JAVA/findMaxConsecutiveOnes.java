package edu.ucsc;

/**
 * Leetcode Number: 485
 * Problem Name: Max Consecutive Ones
 *
 * @ author: Created by Xiaotong Li 
 * @ time: 6/26/18:2018-06-26 09:13.
 */
public class findMaxConsecutiveOnes {
    public int findMaxConsecutiveOnes(int[] nums) {
        int maxHere = 0, max = 0;
        for (int i : nums)
            max = Math.max(max, maxHere = i == 0 ? 0 : maxHere + 1);
        return max;
    }
}
