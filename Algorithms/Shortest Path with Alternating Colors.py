You are given an integer n, the number of nodes in a directed graph where the nodes are labeled from 0 to n - 1. Each edge is red or blue in this graph, and there could be self-edges and parallel edges.

You are given two arrays redEdges and blueEdges where:

redEdges[i] = [ai, bi] indicates that there is a directed red edge from node ai to node bi in the graph, and
blueEdges[j] = [uj, vj] indicates that there is a directed blue edge from node uj to node vj in the graph.
Return an array answer of length n, where each answer[x] is the length of the shortest path from node 0 to node x such that the edge colors alternate along the path, or -1 if such a path does not exist.

 

Example 1:

Input: n = 3, redEdges = [[0,1],[1,2]], blueEdges = []
Output: [0,1,-1]
Example 2:

Input: n = 3, redEdges = [[0,1]], blueEdges = [[2,1]]
Output: [0,1,-1]
 

Constraints:

1 <= n <= 100
0 <= redEdges.length, blueEdges.length <= 400
redEdges[i].length == blueEdges[j].length == 2
0 <= ai, bi, uj, vj < n





from collections import deque, defaultdict
from typing import List

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        # Initialize adjacency lists for red and blue edges
        red_graph = defaultdict(list)
        blue_graph = defaultdict(list)
        
        for u, v in redEdges:
            red_graph[u].append(v)
        for u, v in blueEdges:
            blue_graph[u].append(v)
        
        # Result array with -1 as default value
        result = [-1] * n
        result[0] = 0  # Distance to the starting node is 0
        
        # Queue for BFS: (current_node, current_color, current_distance)
        queue = deque([(0, 'R', 0), (0, 'B', 0)])
        
        # Visited set to track (node, color)
        visited = set([(0, 'R'), (0, 'B')])
        
        while queue:
            node, color, distance = queue.popleft()
            
            # Determine the next edges to explore based on the current edge color
            if color == 'R':
                next_edges = blue_graph[node]
                next_color = 'B'
            else:
                next_edges = red_graph[node]
                next_color = 'R'
            
            for neighbor in next_edges:
                if (neighbor, next_color) not in visited:
                    visited.add((neighbor, next_color))
                    queue.append((neighbor, next_color, distance + 1))
                    
                    # Update the result array if it's the first time reaching this node or if we found a shorter path
                    if result[neighbor] == -1:
                        result[neighbor] = distance + 1
                    else:
                        result[neighbor] = min(result[neighbor], distance + 1)
        
        return result
