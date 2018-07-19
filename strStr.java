package edu.ucsc;

import java.lang.String;

/**
 * Leetcode Number: 28
 * Problem Name: Implement strStr()
 *
 * @author: Created by Xiaotong Li 
 * @time: 7/4/18:2018-07-04 09:00.
 */

public class strStr {
    public int strStr(String haystack, String needle){
        for (int i = 0; ; i++){
            for (int j = 0; ; j++) {
                if (j == needle.length()) return i;
                if (i + j == haystack.length()) return -1;
                if (needle.charAt(j) != haystack.charAt(i + j)) break;
            }
        }
    }
}
