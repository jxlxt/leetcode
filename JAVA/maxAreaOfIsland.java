package edu.ucsc;


/**
 * Leetcode Number: 695
 * Problem Name: Max Area of Island
 *
 * @author: Created by Xiaotong Li 
 * @time: 6/20/18:2018-06-20 18:59.
 */
public class maxAreaOfIsland {
    public int maxAreaOfIsland(int[][] grid) {
        int max_area = 0;
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] == 1) {
                    max_area = Math.max(max_area, helper(grid, i, j));
                }
            }
        }
        return max_area;
    }

    public int helper(int[][] grid, int i, int j){
        if (i >= 0 && i < grid.length && j >= 0 && j < grid[0].length && grid[i][j] == 1) {
            grid[i][j] = 0;
            return 1 + helper(grid, i - 1, j) + helper(grid, i + 1, j) + helper(grid, i, j - 1) + helper(grid, i, j + 1);
        }
        return 0;
    }
}
