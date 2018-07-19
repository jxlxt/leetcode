package edu.ucsc;

import java.util.HashSet;

/**
 * Leetcode Number: 575
 * Problem Name: Distribute Candies
 *
 * @author: Created by Xiaotong Li 
 * @time: 7/3/18:2018-07-03 09:32.
 */
public class distributeCandies {
    public int distributeCandies(int[] candies) {
        HashSet<Integer> set = new HashSet<Integer>();
        for (int candy:candies) {
            set.add(candy);
        }
        return Math.min(set.size(), candies.length/2);
    }
}
