package edu.ucsc;

/**
 * Leetcode Number: 832
 * Problem Name: Flipping an Image
 *
 * @author: Created by Xiaotong Li 
 * @time: 6/28/18:2018-06-28 09:12.
 */

/**
 * We can do this in place.
 * In each row, the ith value from the left is equal to the
 * inverse of the ith value from the right.

 * We use (C+1) / 2 (with floor division) to
 * iterate over all indexes i in the first
 * half of the row, including the center.
 */
public class flipAndInvertImage {
    public int[][] flipAndInvertImage(int[][] A) {
        int C = A[0].length;
        for (int[] row: A){
            for (int i = 0; i < (C + 1)/2; ++i) {
                int tmp = row[i] ^ 1;
                row[i] = row[C - 1 - i] ^ 1;
                row[C - 1 - i] = tmp;
            }
        }
        return A;
    }
}
