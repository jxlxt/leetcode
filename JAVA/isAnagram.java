package edu.ucsc;

/**
 * Leetcode Number: 242
 * Problem Name: Valid Anagram
 *
 * @author: Created by Xiaotong Li 
 * @time: 6/30/18:2018-06-30 22:50.
 */
public class isAnagram {
    public boolean isAnagram(String s, String t) {
        int[] alphabet = new  int[26];
        for (int i = 0; i < s.length(); i++) alphabet[s.charAt(i) - 'a']++;
        for (int i = 0; i < t.length(); i++) alphabet[t.charAt(i) - 'a']--;
        for (int i: alphabet) if (alphabet[i] != 0) return false;
        return true;
    }
}
