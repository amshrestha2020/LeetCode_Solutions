There are n cities numbered from 1 to n. You are given an array edges of size n-1, where edges[i] = [ui, vi] represents a bidirectional edge between cities ui and vi. There exists a unique path between each pair of cities. In other words, the cities form a tree.

A subtree is a subset of cities where every city is reachable from every other city in the subset, where the path between each pair passes through only the cities from the subset. Two subtrees are different if there is a city in one subtree that is not present in the other.

For each d from 1 to n-1, find the number of subtrees in which the maximum distance between any two cities in the subtree is equal to d.

Return an array of size n-1 where the dth element (1-indexed) is the number of subtrees in which the maximum distance between any two cities is equal to d.

Notice that the distance between the two cities is the number of edges in the path between them.

 

Example 1:



Input: n = 4, edges = [[1,2],[2,3],[2,4]]
Output: [3,4,0]
Explanation:
The subtrees with subsets {1,2}, {2,3} and {2,4} have a max distance of 1.
The subtrees with subsets {1,2,3}, {1,2,4}, {2,3,4} and {1,2,3,4} have a max distance of 2.
No subtree has two nodes where the max distance between them is 3.
Example 2:

Input: n = 2, edges = [[1,2]]
Output: [1]
Example 3:

Input: n = 3, edges = [[1,2],[2,3]]
Output: [2,1]
 

Constraints:

2 <= n <= 15
edges.length == n-1
edges[i].length == 2
1 <= ui, vi <= n
All pairs (ui, vi) are distinct.




from collections import deque
from typing import List

class Solution:
    def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        for e in edges:
            graph[e[0]-1].append(e[1]-1)
            graph[e[1]-1].append(e[0]-1)
        ans = [0] * (n - 1)
        for state in range(1, 1 << n):
            d = self.maxDistance(state, graph, n)
            if d > 0: ans[d - 1] += 1
        return ans

    def maxDistance(self, state, graph, n):
        anyNode = cntCity = 0
        for i in range(n):
            if (state >> i) & 1:
                anyNode = i
                cntCity += 1
        farthestNode, _, visitedSize = self.bfs(anyNode, state, graph, n)
        if visitedSize < cntCity: return 0
        _, dist, _ = self.bfs(farthestNode, state, graph, n)
        return dist

    def bfs(self, src, state, graph, n):
        visited = {src}
        q = deque([(src, 0)])
        farthestNode = farthestDist = 0
        while q:
            u, d = q.popleft()
            farthestNode, farthestDist = u, d
            for v in graph[u]:
                if v not in visited and (state >> v) & 1:
                    q.append((v, d + 1))
                    visited.add(v)
        return farthestNode, farthestDist, len(visited)
