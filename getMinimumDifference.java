package edu.ucsc;

/**
 * Leetcode Number: 530
 * Problem Name: Minimum Absolute Difference in BST
 *
 * @author: Created by Xiaotong Li 
 * @time: 7/4/18:2018-07-04 21:08.
 */

/**
 *
 * The most common idea is to first inOrder traverse
 * the tree and compare the delta between each of
 * the adjacent values. It's guaranteed to have
 * the correct answer because it is a BST thus inOrder
 * traversal values are sorted.
 *
 * Solution 1 - In-Order traverse,
 * time complexity O(N),
 * space complexity O(1).
 */
//public class getMinimumDifference {
//    int min = Integer.MAX_VALUE;
//    Integer prev = null;
//
//    public int getMinimumDifference(TreeNode root) {
//        if (root == null) return min;
//        getMinimumDifference(root.left);
//        if (prev != null) {
//            min = Math.min(min, root.val - prev);
//        }
//        prev = root.val;
//        getMinimumDifference(root.right);
//        return min;
//    }
//}
// Follow-up question: If it is not a BST
// The idea is to put the values in TreeSet and use O(lgN) time
// to look up the nearest values.

import java.util.TreeSet;

/**
 * Solution 2: Pre-order Traverse
 * Time-Complexity: O(NlgN)
 * Space-Complexity: O(n)
 *
 */
public class getMinimumDifference {
    TreeSet<Integer> set = new TreeSet<Integer>();
    int min = Integer.MAX_VALUE;

    public int getMinimumDifference(TreeNode root) {
        if (root == null) return min;

        if (!set.isEmpty()) {
            if (set.floor(root.val) != null) {
                min = Math.min(min, root.val - set.floor(root.val));
            }
            if (set.ceiling(root.val) != null) {
                min = Math.min(min, set.ceiling(root.val) - root.val);
            }
        }

        set.add(root.val);

        getMinimumDifference(root.left);
        getMinimumDifference(root.right);

        return min;
    }
}