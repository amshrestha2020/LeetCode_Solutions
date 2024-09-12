There is an undirected weighted connected graph. You are given a positive integer n which denotes that the graph has n nodes labeled from 1 to n, and an array edges where each edges[i] = [ui, vi, weighti] denotes that there is an edge between nodes ui and vi with weight equal to weighti.

A path from node start to node end is a sequence of nodes [z0, z1, z2, ..., zk] such that z0 = start and zk = end and there is an edge between zi and zi+1 where 0 <= i <= k-1.

The distance of a path is the sum of the weights on the edges of the path. Let distanceToLastNode(x) denote the shortest distance of a path between node n and node x. A restricted path is a path that also satisfies that distanceToLastNode(zi) > distanceToLastNode(zi+1) where 0 <= i <= k-1.

Return the number of restricted paths from node 1 to node n. Since that number may be too large, return it modulo 109 + 7.

 

Example 1:


Input: n = 5, edges = [[1,2,3],[1,3,3],[2,3,1],[1,4,2],[5,2,2],[3,5,1],[5,4,10]]
Output: 3
Explanation: Each circle contains the node number in black and its distanceToLastNode value in blue. The three restricted paths are:
1) 1 --> 2 --> 5
2) 1 --> 2 --> 3 --> 5
3) 1 --> 3 --> 5
Example 2:


Input: n = 7, edges = [[1,3,1],[4,1,2],[7,3,4],[2,5,3],[5,6,1],[6,7,2],[7,5,3],[2,6,4]]
Output: 1
Explanation: Each circle contains the node number in black and its distanceToLastNode value in blue. The only restricted path is 1 --> 3 --> 7.
 

Constraints:

1 <= n <= 2 * 104
n - 1 <= edges.length <= 4 * 104
edges[i].length == 3
1 <= ui, vi <= n
ui != vi
1 <= weighti <= 105
There is at most one edge between any two nodes.
There is at least one path between any two nodes.







class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:

        import heapq
        from collections import defaultdict
        from typing import List

        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        
        # Step 2: Compute shortest distances from node `n` using Dijkstra's algorithm
        def dijkstra(start):
            dist = [float('inf')] * (n + 1)
            dist[start] = 0
            min_heap = [(0, start)]
            while min_heap:
                d, u = heapq.heappop(min_heap)
                if d > dist[u]:
                    continue
                for v, weight in graph[u]:
                    if dist[u] + weight < dist[v]:
                        dist[v] = dist[u] + weight
                        heapq.heappush(min_heap, (dist[v], v))
            return dist
        
        dist_to_last_node = dijkstra(n)
        
        # Step 3: DP to count restricted paths from node 1 to node n
        dp = [0] * (n + 1)
        dp[n] = 1
        mod = 10**9 + 7
        
        # Nodes sorted by their distance to the last node in ascending order
        nodes = list(range(1, n + 1))
        nodes.sort(key=lambda x: dist_to_last_node[x])
        
        for u in nodes:
            for v, weight in graph[u]:
                if dist_to_last_node[u] > dist_to_last_node[v]:
                    dp[u] = (dp[u] + dp[v]) % mod
        
        return dp[1]