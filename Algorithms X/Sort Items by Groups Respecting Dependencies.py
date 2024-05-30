There are n items each belonging to zero or one of m groups where group[i] is the group that the i-th item belongs to and it's equal to -1 if the i-th item belongs to no group. The items and the groups are zero indexed. A group can have no item belonging to it.

Return a sorted list of the items such that:

The items that belong to the same group are next to each other in the sorted list.
There are some relations between these items where beforeItems[i] is a list containing all the items that should come before the i-th item in the sorted array (to the left of the i-th item).
Return any solution if there is more than one solution and return an empty list if there is no solution.

 

Example 1:



Input: n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3,6],[],[],[]]
Output: [6,3,4,1,5,2,0,7]
Example 2:

Input: n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3],[],[4],[]]
Output: []
Explanation: This is the same as example 1 except that 4 needs to be before 6 in the sorted list.
 

Constraints:

1 <= m <= n <= 3 * 104
group.length == beforeItems.length == n
-1 <= group[i] <= m - 1
0 <= beforeItems[i].length <= n - 1
0 <= beforeItems[i][j] <= n - 1
i != beforeItems[i][j]
beforeItems[i] does not contain duplicates elements.



from collections import defaultdict, deque
from typing import List

class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        # Adjust group ids for items that are not in any group
        for i in range(n):
            if group[i] == -1:
                group[i] = m
                m += 1
        
        # Initialize graphs and in-degrees
        item_graph = defaultdict(list)
        item_indegree = [0] * n
        group_graph = defaultdict(list)
        group_indegree = [0] * m
        
        # Build the graphs
        for curr in range(n):
            for prev in beforeItems[curr]:
                item_graph[prev].append(curr)
                item_indegree[curr] += 1
                if group[curr] != group[prev]:
                    group_graph[group[prev]].append(group[curr])
                    group_indegree[group[curr]] += 1
        
        # Helper function for topological sort
        def topological_sort(graph, indegree):
            zero_indegree_queue = deque([node for node in range(len(indegree)) if indegree[node] == 0])
            topo_order = []
            
            while zero_indegree_queue:
                node = zero_indegree_queue.popleft()
                topo_order.append(node)
                
                for neighbor in graph[node]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        zero_indegree_queue.append(neighbor)
            
            return topo_order if len(topo_order) == len(indegree) else []
        
        # Get topological orders
        item_order = topological_sort(item_graph, item_indegree)
        if not item_order:
            return []
        
        group_order = topological_sort(group_graph, group_indegree)
        if not group_order:
            return []
        
        # Group items by their group
        group_to_items = defaultdict(list)
        for item in item_order:
            group_to_items[group[item]].append(item)
        
        # Merge the groups in topological order
        result = []
        for grp in group_order:
            result.extend(group_to_items[grp])
        
        return result

