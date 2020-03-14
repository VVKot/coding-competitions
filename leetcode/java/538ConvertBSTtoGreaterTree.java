package leetcode.java;

/**
 * T: O(N) S: O(N)
 *
 * Find the sum of all of the nodes in right subtree and add it to root. Now pass the value of the
 * root to the left subtree, as root and it's right subtree are the values that are guaranteed to be
 * greater. Add all of the values of the nodes in the left subtree to this sum, and return it to the
 * previous caller since it's the total sum of the subtree starting at root.
 */
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int x) {
        val = x;
    }
}


class Solution {
    public TreeNode convertBST(TreeNode root) {
        calculateGreaterTree(root, 0);
        return root;
    }

    public int calculateGreaterTree(TreeNode root, int totalSoFar) {
        if (root == null) {
            return totalSoFar;
        }
        root.val += calculateGreaterTree(root.right, totalSoFar);
        return calculateGreaterTree(root.left, root.val);
    }
}
