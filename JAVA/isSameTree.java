package edu.ucsc;

/**
 * Leetcode Number: 100
 * Problem Name: Same Tree
 *
 * @author: Created by Xiaotong Li 
 * @time: 6/20/18:2018-06-20 09:42.
 */
public class isSameTree {
    private boolean isSameTree(TreeNode p, TreeNode q) {
        if (p == null && q == null) {
            return true;
        }
        if (p == null || q == null) {
            return false;
        }
        if (p.val == q.val) {
            return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
        }
        return false;
    }
}
