package edu.ucsc;

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

/**
 * Leetcode Number: 111
 * Leetcode Problem: Minimum Depth of Binary Tree
 * @time:  05/18/2018, 05:02 PM
 * @author: Xiaotong Li
 */

public class minDepth {
    public int minDepth(TreeNode root) {
        if (root == null) {
            return 0;
        }else if (root.left == null) {
            return minDepth(root.right) + 1;
        }else if (root.right == null) {
            return minDepth(root.left) + 1;
        }
        return Math.min(minDepth(root.left), minDepth(root.right)) + 1;
    }
}
