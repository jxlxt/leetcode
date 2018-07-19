package edu.ucsc;

/**
 * Leetcode Number: 840
 * Problem Name: Magic Squares In Grid
 *
 * @author: Created by Xiaotong Li 
 * @time: 6/28/18:2018-06-28 09:20.
 */
public class numMagicSquaresInside {
    public int numMagicSquaresInside(int[][] grid) {
        int row = grid.length, col = grid[0].length;
        int ans = 0;
        for (int i = 0; i < row - 2; ++i){
            for (int j = 0; j < col - 2; ++j) {
                if (magic(grid[i][j],grid[i][j+1],grid[i][j+2],
                          grid[i+1][j], grid[i+1][j+1],grid[i+1][j+2],
                        grid[i+2][j],grid[i+2][j+1],grid[i+2][j+2]))
                    ans++;
            }
        }
        return ans;
    }
    private boolean magic(int...vals) {
        int[] count = new int[16];
        for (int v: vals) count[v]++;
        for (int v = 1; v <= 9; ++v) {
            if (count[v] != 1) return false;
        }
        return (vals[0] + vals[1] + vals[2] == 15 &&
                vals[3] + vals[4] + vals[5] == 15 &&
                vals[6] + vals[7] + vals[8] == 15 &&
                vals[0] + vals[3] + vals[6] == 15 &&
                vals[1] + vals[4] + vals[7] == 15 &&
                vals[2] + vals[5] + vals[8] == 15 &&
                vals[0] + vals[4] + vals[8] == 15 &&
                vals[2] + vals[4] + vals[6] == 15);
    }

}
