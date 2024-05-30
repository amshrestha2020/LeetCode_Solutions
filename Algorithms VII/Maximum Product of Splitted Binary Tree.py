Given the root of a binary tree, split the binary tree into two subtrees by removing one edge such that the product of the sums of the subtrees is maximized.

Return the maximum product of the sums of the two subtrees. Since the answer may be too large, return it modulo 109 + 7.

Note that you need to maximize the answer before taking the mod and not after taking it.

 

Example 1:


Input: root = [1,2,3,4,5,6]
Output: 110
Explanation: Remove the red edge and get 2 binary trees with sum 11 and 10. Their product is 110 (11*10)
Example 2:


Input: root = [1,null,2,3,4,null,null,5,6]
Output: 90
Explanation: Remove the red edge and get 2 binary trees with sum 15 and 6.Their product is 90 (15*6)
 

Constraints:

The number of nodes in the tree is in the range [2, 5 * 104].
1 <= Node.val <= 104




class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10**9 + 7
        # Calculate the total sum of all nodes in the tree
        total_sum = self.dfs(root)
        # Initialize the maximum product
        self.max_product = 0
        # Calculate the sum of each subtree and find the maximum product
        self.dfs(root, total_sum)
        # Return the maximum product modulo 10^9 + 7
        return self.max_product % MOD

    def dfs(self, node, total_sum=None):
        if not node:
            return 0
        # Calculate the sum of the subtree rooted at this node
        subtree_sum = node.val + self.dfs(node.left, total_sum) + self.dfs(node.right, total_sum)
        # If the total sum is given, find the maximum product
        if total_sum is not None:
            self.max_product = max(self.max_product, subtree_sum * (total_sum - subtree_sum))
        # Return the sum of the subtree rooted at this node
        return subtree_sum
