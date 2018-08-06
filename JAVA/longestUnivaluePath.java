package edu.ucsc;

/**
 * Leetcode Number: 687
 * Problem Name: Longest Univalue Path
 *
 * @author: Created by Xiaotong Li 
 * @time: 7/4/18:2018-07-04 20:51.
 */
public class longestUnivaluePath {
    int len = 0;
    public int longestUnivaluePath(TreeNode root) {
        if (root == null) return 0;
        len = 0;
        getLen(root, root.val);
        return len;
    }

    private int getLen(TreeNode node, int val) {
        if (node == null) return 0;
        int left = getLen(node.left, node.val);
        int right = getLen(node.right, node.val);
        len = Math.max(len, right + left);
        if (val == node.val) return Math.max(left, right) + 1;
        return 0;
    }
}
