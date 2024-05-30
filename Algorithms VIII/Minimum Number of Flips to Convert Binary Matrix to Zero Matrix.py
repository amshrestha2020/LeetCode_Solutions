Given a m x n binary matrix mat. In one step, you can choose one cell and flip it and all the four neighbors of it if they exist (Flip is changing 1 to 0 and 0 to 1). A pair of cells are called neighbors if they share one edge.

Return the minimum number of steps required to convert mat to a zero matrix or -1 if you cannot.

A binary matrix is a matrix with all cells equal to 0 or 1 only.

A zero matrix is a matrix with all cells equal to 0.

 

Example 1:


Input: mat = [[0,0],[0,1]]
Output: 3
Explanation: One possible solution is to flip (1, 0) then (0, 1) and finally (1, 1) as shown.
Example 2:

Input: mat = [[0]]
Output: 0
Explanation: Given matrix is a zero matrix. We do not need to change it.
Example 3:

Input: mat = [[1,0,0],[1,0,0]]
Output: -1
Explanation: Given matrix cannot be a zero matrix.
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 3
mat[i][j] is either 0 or 1.



from typing import List
from collections import deque

class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        start = sum(cell << (i * n + j) for i, row in enumerate(mat) for j, cell in enumerate(row))
        queue = deque([(start, 0)])
        visited = {start}
        while queue:
            node, depth = queue.popleft()
            if node == 0: return depth
            for x in range(m):
                for y in range(n):
                    next_node = node
                    for dx, dy in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1), (x, y)]:
                        if 0 <= dx < m and 0 <= dy < n:
                            next_node ^= 1 << (dx * n + dy)
                    if next_node not in visited:
                        queue.append((next_node, depth + 1))
                        visited.add(next_node)
        return -1

