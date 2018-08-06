package edu.ucsc;

/**
 * Leetcode Number: 125
 * Problem Name: Valid Palindrome
 *
 * @author: Created by Xiaotong Li 
 * @time: 7/4/18:2018-07-04 09:18.
 */
/**
 * 1. go through the Sting
 * 2. remove all the random/alphanumeric characters
 * 3. compare if it is palindrome?
 *      first, check the start/end index of the string, compare if
 *      two chars are equal.
 *      If so, continue.
 *      If not, return false.
 */
public class isPalindromeII {
    public boolean isPalindrome(String s) {
        if (s == null || s.length() == 0) return true;
        //a - z, A - Z, 0 - 9
        StringBuffer sb = new StringBuffer();
        s = s.toLowerCase();
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if ((c <= 'z' && c >= 'a') || (c >= '0' && c <= '9')) {
                sb.append(c);
            }
        }
        s = sb.toString();
        // check
        int start = 0;
        int end = s.length() - 1;
        while (start < end) {
            if (s.charAt(start) != s.charAt(end)) return false;
            start++;
            end--;
        }
        return true;
    }
}
