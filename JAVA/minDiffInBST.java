package edu.ucsc;

/**
 * Leetcode Number: 783
 * Problem Name: Minimum Distance Between BST Nodes
 *
 * @author: Created by Xiaotong Li 
 * @time: 7/4/18:2018-07-04 21:29.
 */

/**
 * same as the problem 530
 * Minimum Absolute Difference in BST
 */
public class minDiffInBST {
    int min = Integer.MAX_VALUE;
    Integer prev = null;

    public int minDiffInBST(TreeNode root) {
        if (root == null) return min;
        minDiffInBST(root.left);
        if (prev != null) {
            min = Math.min(min, root.val - prev);
        }
        prev = root.val;
        minDiffInBST(root.right);
        return min;
    }
}
