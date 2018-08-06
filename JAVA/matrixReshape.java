package edu.ucsc;

/**
 * Leetcode Number: 566
 * Problem Name: Reshape the Matrix
 *
 * @author: Created by Xiaotong Li 
 * @time: 6/26/18:2018-06-26 19:11.
 */
public class matrixReshape {
    public int[][] matrixReshape(int[][] nums, int r, int c) {
            int n = nums.length, m = nums[0].length;
            if (r*c != m*n) return nums;
            int[][] res = new int[r][c];
            for (int i = 0; i < r * c; i++){
                res[i/c] [i%c] = nums[i/m] [i%m];
            }
            return res;
    }
}
