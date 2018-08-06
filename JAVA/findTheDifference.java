package edu.ucsc;

/**
 * Leetcode Number: 389
 * Problem Name: Find the Difference
 *
 * @author: Created by Xiaotong Li 
 * @time: 7/1/18:2018-07-01 11:40.
 */
public class findTheDifference {
    public char findTheDifference(String s, String t) {
        int n = t.length();
        char c = t.charAt(n - 1);
        for (int i = 0; i < n - 1; ++i) {
            c ^= s.charAt(i);
            c ^= t.charAt(i);
        }
        return c;
    }
}
