You have n binary tree nodes numbered from 0 to n - 1 where node i has two children leftChild[i] and rightChild[i], return true if and only if all the given nodes form exactly one valid binary tree.

If node i has no left child then leftChild[i] will equal -1, similarly for the right child.

Note that the nodes have no values and that we only use the node numbers in this problem.

 

Example 1:


Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1]
Output: true
Example 2:


Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,3,-1,-1]
Output: false
Example 3:


Input: n = 2, leftChild = [1,0], rightChild = [-1,-1]
Output: false
 

Constraints:

n == leftChild.length == rightChild.length
1 <= n <= 104
-1 <= leftChild[i], rightChild[i] <= n - 1




class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        # Step 1: Track parent counts
        parent_count = [0] * n
        for i in range(n):
            if leftChild[i] != -1:
                parent_count[leftChild[i]] += 1
            if rightChild[i] != -1:
                parent_count[rightChild[i]] += 1
        
        # Step 2: Identify the root
        root_count = 0
        root = -1
        for i in range(n):
            if parent_count[i] == 0:
                root_count += 1
                root = i
            elif parent_count[i] > 1:
                return False  # A node has more than one parent
        
        # There should be exactly one root
        if root_count != 1:
            return False
        
        # Step 3: Perform DFS to check reachability and cycles
        visited = [False] * n
        def dfs(node):
            if node == -1:
                return True
            if visited[node]:
                return False  # Cycle detected
            visited[node] = True
            return dfs(leftChild[node]) and dfs(rightChild[node])
        
        if not dfs(root):
            return False
        
        # Step 4: Ensure all nodes are visited exactly once
        return all(visited)
