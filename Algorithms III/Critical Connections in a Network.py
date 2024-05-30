There are n servers numbered from 0 to n - 1 connected by undirected server-to-server connections forming a network where connections[i] = [ai, bi] represents a connection between servers ai and bi. Any server can reach other servers directly or indirectly through the network.

A critical connection is a connection that, if removed, will make some servers unable to reach some other server.

Return all critical connections in the network in any order.

 

Example 1:


Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
Output: [[1,3]]
Explanation: [[3,1]] is also accepted.
Example 2:

Input: n = 2, connections = [[0,1]]
Output: [[0,1]]
 

Constraints:

2 <= n <= 105
n - 1 <= connections.length <= 105
0 <= ai, bi <= n - 1
ai != bi
There are no repeated connections.




from typing import List

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = [[] for _ in range(n)]
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        low = [0] * n
        depth = [-1] * n
        critical = []

        def dfs(node, parent, d):
            depth[node] = d
            low[node] = d
            for neighbor in graph[node]:
                if depth[neighbor] == -1:
                    dfs(neighbor, node, d + 1)
                if neighbor != parent:
                    low[node] = min(low[node], low[neighbor])
                if low[neighbor] > d:
                    critical.append([node, neighbor])

        dfs(0, -1, 0)
        return critical
