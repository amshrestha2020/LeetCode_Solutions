There is a binary tree rooted at 0 consisting of n nodes. The nodes are labeled from 0 to n - 1. You are given a 0-indexed integer array parents representing the tree, where parents[i] is the parent of node i. Since node 0 is the root, parents[0] == -1.

Each node has a score. To find the score of a node, consider if the node and the edges connected to it were removed. The tree would become one or more non-empty subtrees. The size of a subtree is the number of the nodes in it. The score of the node is the product of the sizes of all those subtrees.

Return the number of nodes that have the highest score.

 

Example 1:

example-1
Input: parents = [-1,2,0,2,0]
Output: 3
Explanation:
- The score of node 0 is: 3 * 1 = 3
- The score of node 1 is: 4 = 4
- The score of node 2 is: 1 * 1 * 2 = 2
- The score of node 3 is: 4 = 4
- The score of node 4 is: 4 = 4
The highest score is 4, and three nodes (node 1, node 3, and node 4) have the highest score.
Example 2:

example-2
Input: parents = [-1,2,0]
Output: 2
Explanation:
- The score of node 0 is: 2 = 2
- The score of node 1 is: 2 = 2
- The score of node 2 is: 1 * 1 = 1
The highest score is 2, and two nodes (node 0 and node 1) have the highest score.
 

Constraints:

n == parents.length
2 <= n <= 105
parents[0] == -1
0 <= parents[i] <= n - 1 for i != 0
parents represents a valid binary tree.




class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        from typing import List


        n = len(parents)
        tree = [[] for _ in range(n)]
        
        # Build the tree
        for child in range(1, n):
            tree[parents[child]].append(child)
        
        # Array to hold the sizes of subtrees
        subtree_size = [0] * n

        def dfs(node: int) -> int:
            size = 1  # Count the current node
            for child in tree[node]:
                size += dfs(child)  # Add the size of each child's subtree
            subtree_size[node] = size
            return size
        
        # Start DFS from the root
        dfs(0)
        
        max_score = 0
        count = 0
        
        # Calculate scores for each node
        for node in range(n):
            score = 1
            # Calculate product of sizes of all subtrees formed by removing this node
            for child in tree[node]:
                score *= subtree_size[child]
            
            # Include the size of the "remaining" tree if this is not the root
            if node != 0:
                score *= (n - subtree_size[node])
            
            # Update max score and count
            if score > max_score:
                max_score = score
                count = 1
            elif score == max_score:
                count += 1
        
        return count
    