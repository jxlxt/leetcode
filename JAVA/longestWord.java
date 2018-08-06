package edu.ucsc;

import java.util.Arrays;
import java.util.HashSet;

/**
 * Leetcode Number: 720
 * Problem Name: Longest Word in Dictionary
 *
 * @author: Created by Xiaotong Li 
 * @time: 7/3/18:2018-07-03 22:59.
 */
public class longestWord {
    public String longestWord(String[] words){
        Arrays.sort(words);
        HashSet<String> built = new HashSet<String>();
        String res = "";
        for (String w: words) {
            if (w.length() == 1 || built.contains(w.substring(0, w.length()-1))){
                res = w.length() > res.length() ? w:res;
                built.add(w);
             }
        }
        return res;
    }
}
