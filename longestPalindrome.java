package edu.ucsc;

import java.util.HashSet;

/**
 * Leetcode Number: 409
 * Problem Name: Longest Palindrome
 *
 * @author: Created by Xiaotong Li 
 * @time: 7/1/18:2018-07-01 11:46.
 */

/**
 * Intuition
 *
 * A palindrome consists of letters with equal partners,
 * plus possibly a unique center (without a partner).
 * The letter i from the left has its partner i from the right.
 * For example in 'abcba', 'aa' and 'bb' are partners, and 'c'
 * is a unique center.
 *
 * Imagine we built our palindrome.
 * It consists of as many partnered letters as possible,
 * plus a unique center if possible.
 * This motivates a greedy approach.
 *
 * Algorithm
 *
 * For each letter, say it occurs v times.
 * We know we have v
 * // 2 * 2 letters that can be partnered for sure.
 * For example, if we have 'aaaaa',
 * then we could have 'aaaa' partnered,
 * which is 5 // 2 * 2 = 4 letters partnered.
 *
 * At the end, if there was any v % 2 == 1,
 * then that letter could have been a unique center.
 * Otherwise, every letter was partnered.
 * To perform this check, we will check for v % 2 == 1
 * and ans % 2 == 0, the latter meaning
 * we haven't yet added a unique center to the answer.
 */
public class longestPalindrome {
    public int longestPalindrome(String s) {
        if (s == null || s.length() == 0) return 0;
        HashSet<Character> hs = new HashSet<Character>();
        int count = 0;
        for (int i = 0; i < s.length(); i++) {
            if (hs.contains(s.charAt(i))) {
                hs.remove(s.charAt(i));
                count++;
            }else {
                hs.add(s.charAt(i));
            }
        }
        if (!hs.isEmpty()) return count*2+1;
        return count*2;
    }
}
