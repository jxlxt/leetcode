package edu.ucsc;

import java.util.ArrayList;
import java.util.List;

/**
 * Leetcode Number: 438
 * Problem Name: Find All Anagrams in a String
 *
 * @author: Created by Xiaotong Li 
 * @time: 7/1/18:2018-07-01 12:00.
 */

/**
 * the idea is using sliding window
 */
public class findAnagrams {
    public List<Integer> findAnagrams(String s, String p) {
        List<Integer> list = new ArrayList<Integer>();
        if (s == null || s.length() == 0 || p == null || p.length() ==0) return list;
        int[] hash = new int[256]; // create character hash
        //record each character p into hash
        for (char c: p.toCharArray()){
            hash[c]++;
        }
        //two points, initialize count to p's length
        int left = 0, right = 0, count = p.length();
        while (right < s.length()) {
            //when the count is down to 0, means we found the right anagram
            //then add window's left to result list
            if (hash[s.charAt(right++)]-- >= 1) count--;

            //when the count is down to 0, means we found the right anagram
            //then add window's left to result list
            if (count == 0) list.add(left);

            //if we find the window's size equals to p, then we have to move left (narrow the window) to find the new match window
            //++ to reset the hash because we kicked out the left
            //only increase the count if the character is in p
            //the count >= 0 indicate it was original in the hash, cuz it won't go below 0
            if (right - left == p.length() && hash[s.charAt(left++)]++ >= 0) count++;
        }
        return list;
    }
}
