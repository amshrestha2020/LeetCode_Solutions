You are asked to cut off all the trees in a forest for a golf event. The forest is represented as an m x n matrix. In this matrix:

0 means the cell cannot be walked through.
1 represents an empty cell that can be walked through.
A number greater than 1 represents a tree in a cell that can be walked through, and this number is the tree's height.
In one step, you can walk in any of the four directions: north, east, south, and west. If you are standing in a cell with a tree, you can choose whether to cut it off.

You must cut off the trees in order from shortest to tallest. When you cut off a tree, the value at its cell becomes 1 (an empty cell).

Starting from the point (0, 0), return the minimum steps you need to walk to cut off all the trees. If you cannot cut off all the trees, return -1.

Note: The input is generated such that no two trees have the same height, and there is at least one tree needs to be cut off.

 

Example 1:


Input: forest = [[1,2,3],[0,0,4],[7,6,5]]
Output: 6
Explanation: Following the path above allows you to cut off the trees from shortest to tallest in 6 steps.
Example 2:


Input: forest = [[1,2,3],[0,0,0],[7,6,5]]
Output: -1
Explanation: The trees in the bottom row cannot be accessed as the middle row is blocked.
Example 3:

Input: forest = [[2,3,4],[0,0,5],[8,7,6]]
Output: 6
Explanation: You can follow the same path as Example 1 to cut off all the trees.
Note that you can cut off the first tree at (0, 0) before making any steps.
 

Constraints:

m == forest.length
n == forest[i].length
1 <= m, n <= 50
0 <= forest[i][j] <= 109
Heights of all trees are distinct.




from typing import List
import heapq

class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        # Get the list of trees.
        trees = sorted((v, r, c) for r, row in enumerate(forest)
                       for c, v in enumerate(row) if v > 1)
        # Initialize the starting point.
        sr = sc = ans = 0
        # For each tree, starting from the smallest,
        for _, tr, tc in trees:
            # Compute the Manhattan distance from the current position.
            d = self.bfs(forest, sr, sc, tr, tc)
            # If the tree cannot be reached, return -1.
            if d < 0: return -1
            # Otherwise, add the distance to the answer,
            # and move to the tree's location.
            else: ans += d
            sr, sc = tr, tc
        return ans

    def bfs(self, forest, sr, sc, tr, tc):
        R, C = len(forest), len(forest[0])
        queue = [(0, sr, sc)]
        seen = {(sr, sc)}
        while queue:
            d, r, c = heapq.heappop(queue)
            # If we've reached the target, return the distance.
            if r == tr and c == tc: return d
            # Otherwise, add the unvisited neighbors to the queue.
            for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                if (0 <= nr < R and 0 <= nc < C and
                    (nr, nc) not in seen and forest[nr][nc]):
                    seen.add((nr, nc))
                    heapq.heappush(queue, (d+1, nr, nc))
        # If we cannot reach the target, return -1.
        return -1
