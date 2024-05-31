Alice is throwing n darts on a very large wall. You are given an array darts where darts[i] = [xi, yi] is the position of the ith dart that Alice threw on the wall.

Bob knows the positions of the n darts on the wall. He wants to place a dartboard of radius r on the wall so that the maximum number of darts that Alice throws lie on the dartboard.

Given the integer r, return the maximum number of darts that can lie on the dartboard.

 

Example 1:


Input: darts = [[-2,0],[2,0],[0,2],[0,-2]], r = 2
Output: 4
Explanation: Circle dartboard with center in (0,0) and radius = 2 contain all points.
Example 2:


Input: darts = [[-3,0],[3,0],[2,6],[5,4],[0,9],[7,8]], r = 5
Output: 5
Explanation: Circle dartboard with center in (0,4) and radius = 5 contain all points except the point (7,8).
 

Constraints:

1 <= darts.length <= 100
darts[i].length == 2
-104 <= xi, yi <= 104
All the darts are unique
1 <= r <= 5000



from typing import List
import math

class Solution:
    def numPoints(self, darts: List[List[int]], r: int) -> int:
        def dist(a, b):
            return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

        n = len(darts)
        res = 1
        for i in range(n):
            for j in range(i+1, n):
                d = dist(darts[i], darts[j])
                if d > 2 * r:
                    continue
                x0 = (darts[i][0] + darts[j][0]) / 2 + (darts[i][1] - darts[j][1]) * math.sqrt(r * r - d * d / 4) / d
                y0 = (darts[i][1] + darts[j][1]) / 2 + (darts[j][0] - darts[i][0]) * math.sqrt(r * r - d * d / 4) / d
                cnt = 0
                for k in range(n):
                    if dist([x0, y0], darts[k]) <= r + 1e-8:
                        cnt += 1
                res = max(res, cnt)
        return res
