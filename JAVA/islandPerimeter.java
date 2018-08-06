package edu.ucsc;

/**
 * Leetcode Number: 463
 * Problem Name: Island Perimeter
 *
 * @author: Created by Xiaotong Li 
 * @time: 7/3/18:2018-07-03 08:56.
 */
//loop over the matrix and count the number of islands;
//        if the current dot is an island,
// count if it has any right neighbour or down neighbour;
//the result is islands * 4 - neighbours * 2

public class islandPerimeter {
    public int islandPerimeter(int[][] grid) {
        int islands = 0, neighbour = 0;
        for (int i = 0; i < grid.length; i++){
            for (int j = 0; j < grid[i].length; j++) {
                if (grid[i][j] == 1) {
                    islands++;//count the number of islands
                    //count the down neighbour
                    if (i < grid.length - 1 && grid[i+1][j] == 1) neighbour++;
                    //count the right neighbour
                    if (j < grid[i].length - 1 && grid[i][j+1] == 1) neighbour++;
                }
            }
        }
        return islands * 4 - neighbour * 2;
    }
}
