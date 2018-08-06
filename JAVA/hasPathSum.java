package edu.ucsc;


/**
 * Leetcode Number:112
 * Problem Name:Path Sum
 *
 * @author: Created by Xiaotong Li 
 * @time: 6/20/18:2018-06-20 18:50.
 */
public class hasPathSum {
    public boolean hasPathSum(TreeNode root, int sum) {
        if (root == null) {
            return false;
        }
        if (root.left == null && root.right == null && sum - root.val == 0) {
            return true;
        }
        return hasPathSum(root.left, sum - root.val) || hasPathSum(root.right, sum - root.val);
    }
}
