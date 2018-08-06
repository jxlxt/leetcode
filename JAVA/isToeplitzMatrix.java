package edu.ucsc;

/**
 * Leetcode Number: 766
 * Problem Name: Toeplitz Matrix
 *
 * @author: Created by Xiaotong Li 
 * @time: 6/27/18:2018-06-27 23:04.
 */
public class isToeplitzMatrix {
    public boolean isToeplitzMatrix(int[][] matrix) {
        for (int i = 0; i < matrix.length - 1; i++) {
            for (int j = 0; j < matrix[i].length - 1; j++) {
                if (matrix[i][j] != matrix[i+1][j+1]) return false;
            }
        }
        return true;
    }
}
