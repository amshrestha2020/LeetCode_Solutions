Given an undirected tree consisting of n vertices numbered from 1 to n. A frog starts jumping from vertex 1. In one second, the frog jumps from its current vertex to another unvisited vertex if they are directly connected. The frog can not jump back to a visited vertex. In case the frog can jump to several vertices, it jumps randomly to one of them with the same probability. Otherwise, when the frog can not jump to any unvisited vertex, it jumps forever on the same vertex.

The edges of the undirected tree are given in the array edges, where edges[i] = [ai, bi] means that exists an edge connecting the vertices ai and bi.

Return the probability that after t seconds the frog is on the vertex target. Answers within 10-5 of the actual answer will be accepted.

 

Example 1:


Input: n = 7, edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], t = 2, target = 4
Output: 0.16666666666666666 
Explanation: The figure above shows the given graph. The frog starts at vertex 1, jumping with 1/3 probability to the vertex 2 after second 1 and then jumping with 1/2 probability to vertex 4 after second 2. Thus the probability for the frog is on the vertex 4 after 2 seconds is 1/3 * 1/2 = 1/6 = 0.16666666666666666. 
Example 2:


Input: n = 7, edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], t = 1, target = 7
Output: 0.3333333333333333
Explanation: The figure above shows the given graph. The frog starts at vertex 1, jumping with 1/3 = 0.3333333333333333 probability to the vertex 7 after second 1. 
 

Constraints:

1 <= n <= 100
edges.length == n - 1
edges[i].length == 2
1 <= ai, bi <= n
1 <= t <= 50
1 <= target <= n




from collections import deque

class Solution:
    def frogPosition(self, n, edges, t, target):
        graph = [[] for _ in range(n+1)]
        visited = [False] * (n+1)

        for edge in edges:
            u, v = edge
            graph[u].append(v)
            graph[v].append(u)

        graph[1].append(0)
        q = deque()
        q.append((1, 1.00))
        visited[1] = True
        level = 0

        while q:
            len_q = len(q)

            for _ in range(len_q):
                currentNodeIdx, currentNodeProb = q.popleft()

                if currentNodeIdx == target:
                    if len(graph[currentNodeIdx]) == 1 and t >= level:
                        return currentNodeProb
                    elif level == t:
                        return currentNodeProb
                    else:
                        return 0.00

                s = len(graph[currentNodeIdx]) - 1

                if s > 0:  # Check if s is not zero
                    for i in range(len(graph[currentNodeIdx])):
                        child = graph[currentNodeIdx][i]
                        prob = currentNodeProb / s
                        if not visited[child] and child > 0:
                            q.append((child, prob))
                            visited[child] = True

            level += 1

        return 0.00
