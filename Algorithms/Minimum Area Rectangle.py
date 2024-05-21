You are given an array of points in the X-Y plane points where points[i] = [xi, yi].

Return the minimum area of a rectangle formed from these points, with sides parallel to the X and Y axes. If there is not any such rectangle, return 0.

 

Example 1:


Input: points = [[1,1],[1,3],[3,1],[3,3],[2,2]]
Output: 4
Example 2:


Input: points = [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
Output: 2
 

Constraints:

1 <= points.length <= 500
points[i].length == 2
0 <= xi, yi <= 4 * 104
All the given points are unique.




class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        pointSet = set(map(tuple, points))
        minArea = float('inf')

        for i in range(len(points)):
            for j in range(i):
                p1, p2 = points[i], points[j]
                if (p1[0] != p2[0] and p1[1] != p2[1] and
                    (p1[0], p2[1]) in pointSet and
                    (p2[0], p1[1]) in pointSet):
                    minArea = min(minArea, abs(p2[0] - p1[0]) * abs(p2[1] - p1[1]))

        return minArea if minArea < float('inf') else 0
