package edu.ucsc;

/**
 * Leetcode Number: 387
 * Problem Name: First Unique Character in a String
 *
 * @author: Created by Xiaotong Li 
 * @time: 7/1/18:2018-07-01 10:56.
 */
public class firstUniqChar {
    public int firstUniqChar(String s) {
        int freq[] = new int[26];
        for (int i = 0; i < s.length(); i++) {
            freq[s.charAt(i) - 'a']++;
        }
        for (int i = 0; i < s.length(); i++) {
            if (freq[s.charAt(i) - 'a'] == 1){
                return i;
            }
        }
        return -1;
    }
}
