package edu.ucsc;

import java.util.LinkedList;
import java.util.List;

/**
 * Leetcode Number: 784
 * Problem Name: Letter Case Permutation
 *
 * @author: Created by Xiaotong Li 
 * @time: 7/4/18:2018-07-04 23:45.
 */
public class letterCasePermutation {
    public List<String> letterCasePermutation(String S){
        if (S == null) return new LinkedList<String>();
        List<String> res = new LinkedList<String>();
        helper(S, res, 0);
        return res;
    }
    private void helper(String s, List<String> res, int pos) {
        if (pos == s.length()) {
            res.add(s);
            return;
        }
        if (s.charAt(pos) >= '0' && s.charAt(pos) <= '9') {
            helper(s, res, pos + 1);
            return;
        }
        char[] chs = s.toCharArray();
        chs[pos] = Character.toLowerCase(chs[pos]);
        helper(String.valueOf(chs), res, pos + 1);

        chs[pos] = Character.toUpperCase(chs[pos]);
        helper(String.valueOf(chs), res, pos + 1);

    }
}
