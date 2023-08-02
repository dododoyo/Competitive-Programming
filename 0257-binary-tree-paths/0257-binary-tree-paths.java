/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
 class Solution {
    public List<String> binaryTreePaths(TreeNode root) {
      List<String> sol = new ArrayList<>();
      if(root != null) depthFirstSearch(root, "", sol);
      return sol;   
    }
    public void depthFirstSearch(TreeNode root, String path, List<String> sol) {
        if(root.left == null && root.right == null) sol.add(path + root.val);
        if(root.left != null) depthFirstSearch(root.left, path + root.val + "->", sol);
        if(root.right != null) depthFirstSearch(root.right, path + root.val + "->", sol);
    }
}