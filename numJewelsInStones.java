package edu.ucsc;

/**
 * Leetcode Number: 771
 * Problem Name: Jewels and Stones
 *
 * @author: Created by Xiaotong Li 
 * @time: 7/3/18:2018-07-03 23:30.
 */
public class numJewelsInStones {
    public int numJewelsInStones(String J, String S) {
        return S.replaceAll("[^" + J + "]","").length();
    }
}
