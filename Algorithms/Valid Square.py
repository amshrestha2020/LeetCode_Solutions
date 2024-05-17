Given the coordinates of four points in 2D space p1, p2, p3 and p4, return true if the four points construct a square.

The coordinate of a point pi is represented as [xi, yi]. The input is not given in any order.

A valid square has four equal sides with positive length and four equal angles (90-degree angles).

 

Example 1:

Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
Output: true
Example 2:

Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,12]
Output: false
Example 3:

Input: p1 = [1,0], p2 = [-1,0], p3 = [0,1], p4 = [0,-1]
Output: true
 

Constraints:

p1.length == p2.length == p3.length == p4.length == 2
-104 <= xi, yi <= 104




class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def dist(p, q):
            return (p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2

        points = [p1, p2, p3, p4]
        points.sort(key = lambda p: (p[0], p[1]))

        return dist(points[0], points[1]) != 0 and \
               dist(points[0], points[1]) == dist(points[1], points[3]) and \
               dist(points[1], points[3]) == dist(points[3], points[2]) and \
               dist(points[3], points[2]) == dist(points[2], points[0]) and \
               dist(points[0], points[3]) == dist(points[1], points[2])
