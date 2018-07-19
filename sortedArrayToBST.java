package edu.ucsc;

/**
 * Leetcode Number:
 * Problem Name:
 * @author: Created by Xiaotong Li 
 * @time: 5/28/18:2018-05-28 17:24.
 */

public class sortedArrayToBST {
    public TreeNode sortedArrayToBST(int[] num){
        if (num.length == 0){
            return null;
        }
        return helper(num, 0, num.length - 1);
    }

    private TreeNode helper(int[] num, int low, int high ){
        if (low > high - 1){
            return null;
        }
        int mid = (low + high)/2;
        TreeNode node = new TreeNode(num[mid]);
        node.left = helper(num, low, mid - 1);
        node.right = helper(num, mid + 1, high);
        return node;
    }
}
