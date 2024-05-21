Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the values of all nodes that have a distance k from the target node.

You can return the answer in any order.

 

Example 1:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
Output: [7,4,1]
Explanation: The nodes that are a distance 2 from the target node (with value 5) have values 7, 4, and 1.
Example 2:

Input: root = [1], target = 1, k = 3
Output: []
 

Constraints:

The number of nodes in the tree is in the range [1, 500].
0 <= Node.val <= 500
All the values Node.val are unique.
target is the value of one of the nodes in the tree.
0 <= k <= 1000





# Definition for a binary tree node.
from collections import defaultdict
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # Create a graph using DFS
        graph = defaultdict(list)
        def dfs(node, parent=None):
            if node:
                if parent:
                    graph[node.val].append(parent.val)
                    graph[parent.val].append(node.val)
                dfs(node.left, node)
                dfs(node.right, node)
        dfs(root)

        # BFS to find all nodes a distance k from target
        queue = [(target.val, 0)]
        seen = {target.val}
        while queue:
            node, dist = queue.pop(0)
            if dist == k:
                return [node] + [n for n, d in queue if d == k]
            for nei in graph[node]:
                if nei not in seen:
                    seen.add(nei)
                    queue.append((nei, dist+1))
        return []
