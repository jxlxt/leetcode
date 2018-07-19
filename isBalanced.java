package edu.ucsc;

public class isBalanced {

    private static final int UNBALANCED = -99;

    public boolean isBalanced(TreeNode root) {

        return root == null || depth(root) != UNBALANCED;
    }

    private int depth(TreeNode root) {
        if (root == null) {
            return -1;
        }
        int l = depth(root.left); // left subtree
        int r = depth(root.right); // right subtree
        if (l == UNBALANCED || r == UNBALANCED || Math.abs(l - r) > 1) {
            return UNBALANCED;
        }
        return Math.max(l,r) + 1;
    }
}
