package edu.ucsc;

/**
 * Leetcode Number: 746
 * Problem Name: Min Cost Climbing Stairs
 *
 * @author: Created by Xiaotong Li 
 * @time: 6/27/18:2018-06-27 22:21.
 */

/**
 * using dynamic programming method
 */
public class minCostClimbingStairs {
    public int minCostClimbingStairs(int[] cost) {
        int f1 = 0, f2 = 0;
        for (int i = cost.length - 1; i >= 0; --i) {
            int f0 = cost[i] + Math.min(f1, f2);
            f2 = f1;
            f1 = f0;
        }
        return Math.min(f1, f2);
    }
}
