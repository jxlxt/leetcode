package edu.ucsc;

import java.util.ArrayList;
import java.util.List;
         

/**
 * Leetcode Number: 257
 * Problem Name: Binary Tree Paths
 *
 * @author: Created by Xiaotong Li 
 * @time: 5/25/18:2018-05-25 23:13.
 */
public class binaryTreePaths {
        public List<String> binaryTreePaths(TreeNode root) {
            List<String> answer = new ArrayList<String>();
            if (root != null) searchBT(root, "", answer);
            return answer;
        }

        private void searchBT(TreeNode root, String path, List<String> answer){
            if (root.right == null && root.left == null) answer.add(path + root.val);
            if (root.left != null) searchBT(root.left, path + root.val + "->", answer);
            if (root.right != null) searchBT(root.right, path + root.val + "->", answer);
        }
}
