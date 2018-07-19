package edu.ucsc;

import java.util.HashMap;

/**
 * Leetcode Number: 205
 * Problem Name: Isomorphic Strings
 *
 * @author: Created by Xiaotong Li 
 * @time: 6/29/18:2018-06-29 09:17.
 */
// Method 1: Using HashMap
public class isIsomorphic {
    public boolean isIsomorphic(String s, String t) {
        if (s == null || s.length() <= 1) return false;
        HashMap<Character, Character> map = new HashMap<Character, Character>();
        for (int i = 0; i < s.length(); i++) {
            char a = s.charAt(i);
            char b = t.charAt(i);
            if (map.containsKey(a)){
                if (map.get(a).equals(b))
                    continue;
                else
                    return false;
            }else {
                if (!map.containsValue(b)){
                    map.put(a, b);
                }else return false;
            }
        }
        return true;
    }
}
