package edu.ucsc;

//import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * Leetcode Number: 830
 * Problem Name: Positions of Large Groups
 *
 * @author: Created by Xiaotong Li 
 * @time: 6/28/18:2018-06-28 09:04.
 */
public class largeGroupPositions {
    public List<List<Integer>> largeGroupPositions(String S) {
        List<List<Integer>> ans = new ArrayList<List<Integer>>();
        int i = 0, N = S.length();
        for (int j = 0; j < N; ++j) {
            if (j == N - 1 || S.charAt(j) != S.charAt(j + 1)) {
                if (j - i + 1 >= 3) {
                    ans.add(Arrays.asList(new Integer[]{i, j}));
                }
                i = j + 1;
            }
        }
        return ans;
    }
}
