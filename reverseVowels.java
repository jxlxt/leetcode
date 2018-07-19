package edu.ucsc;

/**
 * Leetcode Number: 345
 * Problem Name: Reverse Vowels of a String
 *
 * @author: Created by Xiaotong Li 
 * @time: 7/4/18:2018-07-04 09:45.
 */
public class reverseVowels {
    public String reverseVowels(String s) {
        if (s == null || s.length() == 0) return s;
        String vowels = "aeiouAEIOU";
        char[] chars = s.toCharArray();
        int start = 0;
        int end = s.length() - 1;
        while (start < end) {
            while (start < end && !vowels.contains(chars[start]+"")){
                start++;
            }
            while (start < end && !vowels.contains(chars[end]+"")) {
                end--;
            }
            char temp = chars[start];
            chars[start] = chars[end];
            chars[end] = temp;

            start++;
            end--;
        }
        return new String(chars);
    }
}
