You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns, where heights[row][col] represents the height of cell (row, col). You are situated in the top-left cell, (0, 0), and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.

A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.

Return the minimum effort required to travel from the top-left cell to the bottom-right cell.

 

Example 1:



Input: heights = [[1,2,2],[3,8,2],[5,3,5]]
Output: 2
Explanation: The route of [1,3,5,3,5] has a maximum absolute difference of 2 in consecutive cells.
This is better than the route of [1,2,2,2,5], where the maximum absolute difference is 3.
Example 2:



Input: heights = [[1,2,3],[3,8,4],[5,3,5]]
Output: 1
Explanation: The route of [1,2,3,4,5] has a maximum absolute difference of 1 in consecutive cells, which is better than route [1,3,5,3,5].
Example 3:


Input: heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
Output: 0
Explanation: This route does not require any effort.
 

Constraints:

rows == heights.length
columns == heights[i].length
1 <= rows, columns <= 100
1 <= heights[i][j] <= 106




from heapq import heappop, heappush
from typing import List

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        efforts = [[float('inf')] * n for _ in range(m)]
        efforts[0][0] = 0
        heap = [(0, 0, 0)]  # effort, row, col

        while heap:
            effort, row, col = heappop(heap)
            if (row, col) == (m - 1, n - 1):
                return effort
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < m and 0 <= new_col < n:
                    new_effort = max(effort, abs(heights[new_row][new_col] - heights[row][col]))
                    if efforts[new_row][new_col] > new_effort:
                        efforts[new_row][new_col] = new_effort
                        heappush(heap, (new_effort, new_row, new_col))
