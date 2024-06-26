You are given an array trees where trees[i] = [xi, yi] represents the location of a tree in the garden.

Fence the entire garden using the minimum length of rope, as it is expensive. The garden is well-fenced only if all the trees are enclosed.

Return the coordinates of trees that are exactly located on the fence perimeter. You may return the answer in any order.

 

Example 1:


Input: trees = [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
Output: [[1,1],[2,0],[4,2],[3,3],[2,4]]
Explanation: All the trees will be on the perimeter of the fence except the tree at [2, 2], which will be inside the fence.
Example 2:


Input: trees = [[1,2],[2,2],[4,2]]
Output: [[4,2],[2,2],[1,2]]
Explanation: The fence forms a line that passes through all the trees.
 

Constraints:

1 <= trees.length <= 3000
trees[i].length == 2
0 <= xi, yi <= 100
All the given positions are unique.





class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        if len(trees) == 1:
            return trees

        def orientation(p1, p2, p3):
            return (p2[1] - p1[1]) * (p3[0] - p2[0]) - (p2[0] - p1[0]) * (p3[1] - p2[1])

        def distance(p1, p2):
            return (p2[1] - p1[1]) ** 2 + (p2[0] - p1[0]) ** 2

        # Sort points lexicographically
        trees.sort()

        # Build lower hull
        lower_hull = []
        for tree in trees:
            while len(lower_hull) >= 2 and orientation(lower_hull[-2], lower_hull[-1], tree) < 0:
                lower_hull.pop()
            lower_hull.append(tuple(tree))

        # Build upper hull
        upper_hull = []
        for tree in reversed(trees):
            while len(upper_hull) >= 2 and orientation(upper_hull[-2], upper_hull[-1], tree) < 0:
                upper_hull.pop()
            upper_hull.append(tuple(tree))

        # Combine lower and upper hulls to form convex hull
        convex_hull = lower_hull[:-1] + upper_hull[:-1]

        # Remove duplicate points
        convex_hull = list(set(convex_hull))

        # Sort convex hull points lexicographically
        convex_hull.sort()

        # Convert back to list of lists
        convex_hull = [list(point) for point in convex_hull]

        return convex_hull

