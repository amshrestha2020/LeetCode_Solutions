You are given an array of points in the X-Y plane points where points[i] = [xi, yi].

Return the minimum area of any rectangle formed from these points, with sides not necessarily parallel to the X and Y axes. If there is not any such rectangle, return 0.

Answers within 10-5 of the actual answer will be accepted.

 

Example 1:


Input: points = [[1,2],[2,1],[1,0],[0,1]]
Output: 2.00000
Explanation: The minimum area rectangle occurs at [1,2],[2,1],[1,0],[0,1], with an area of 2.
Example 2:


Input: points = [[0,1],[2,1],[1,1],[1,0],[2,0]]
Output: 1.00000
Explanation: The minimum area rectangle occurs at [1,0],[1,1],[2,1],[2,0], with an area of 1.
Example 3:


Input: points = [[0,3],[1,2],[3,1],[1,3],[2,1]]
Output: 0
Explanation: There is no possible rectangle to form from these points.
 

Constraints:

1 <= points.length <= 50
points[i].length == 2
0 <= xi, yi <= 4 * 104
All the given points are unique.





class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        minArea = 0.0
        if len(points) < 4:
            return 0
        for i in range(len(points) - 3):
            x0, y0 = points[i]
            for j in range(i + 1, len(points)):
                x1, y1 = points[j]
                for k in range(j + 1, len(points)):
                    x2, y2 = points[k]
                    Lx1, Ly1 = x1 - x0, y1 - y0
                    Lx2, Ly2 = x2 - x0, y2 - y0
                    dotProd = Lx1 * Lx2 + Ly1 * Ly2
                    if dotProd != 0:
                        continue
                    skip = True
                    for n in range(len(points)):
                        x3, y3 = points[n]
                        if x3 == x0 + Lx1 + Lx2 and y3 == y0 + Ly1 + Ly2:
                            skip = False
                            break
                    if skip:
                        continue
                    _Area = abs(Lx1 * Ly2 - Ly1 * Lx2)
                    if minArea == 0.0:
                        minArea = _Area
                    else:
                        minArea = min(minArea, _Area)
        return minArea
