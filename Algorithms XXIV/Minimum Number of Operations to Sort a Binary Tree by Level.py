You are given the root of a binary tree with unique values.

In one operation, you can choose any two nodes at the same level and swap their values.

Return the minimum number of operations needed to make the values at each level sorted in a strictly increasing order.

The level of a node is the number of edges along the path between it and the root node.

 

Example 1:


Input: root = [1,4,3,7,6,8,5,null,null,null,null,9,null,10]
Output: 3
Explanation:
- Swap 4 and 3. The 2nd level becomes [3,4].
- Swap 7 and 5. The 3rd level becomes [5,6,8,7].
- Swap 8 and 7. The 3rd level becomes [5,6,7,8].
We used 3 operations so return 3.
It can be proven that 3 is the minimum number of operations needed.
Example 2:


Input: root = [1,3,2,7,6,5,4]
Output: 3
Explanation:
- Swap 3 and 2. The 2nd level becomes [2,3].
- Swap 7 and 4. The 3rd level becomes [4,6,5,7].
- Swap 6 and 5. The 3rd level becomes [4,5,6,7].
We used 3 operations so return 3.
It can be proven that 3 is the minimum number of operations needed.
Example 3:


Input: root = [1,2,3,4,5,6]
Output: 0
Explanation: Each level is already sorted in increasing order so return 0.
 

Constraints:

The number of nodes in the tree is in the range [1, 105].
1 <= Node.val <= 105
All the values of the tree are unique.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        from collections import deque
        from typing import Optional

        if not root:
            return 0
        
        # Initialize a queue for level order traversal
        queue = deque([root])
        total_swaps = 0
        
        while queue:
            level_size = len(queue)
            level_nodes = []
            
            # Collect all nodes at the current level
            for _ in range(level_size):
                node = queue.popleft()
                level_nodes.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # Create a sorted version of the level nodes
            sorted_nodes = sorted(level_nodes)
            
            # Create a mapping from value to index in the original level_nodes
            index_map = {value: i for i, value in enumerate(level_nodes)}
            
            visited = [False] * level_size
            
            # Count cycles to determine the number of swaps needed
            for i in range(level_size):
                if visited[i] or level_nodes[i] == sorted_nodes[i]:
                    continue  # Already in the correct position or visited
                
                # Count the size of the cycle
                cycle_size = 0
                x = i
                
                while not visited[x]:
                    visited[x] = True
                    # Move to the index of the sorted element
                    x = index_map[sorted_nodes[x]]
                    cycle_size += 1
                
                # If there are cycle_size elements, we need cycle_size - 1 swaps
                if cycle_size > 1:
                    total_swaps += cycle_size - 1
        
        return total_swaps