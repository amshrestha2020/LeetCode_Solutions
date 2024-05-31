Given a string s of lowercase letters, you need to find the maximum number of non-empty substrings of s that meet the following conditions:

The substrings do not overlap, that is for any two substrings s[i..j] and s[x..y], either j < x or i > y is true.
A substring that contains a certain character c must also contain all occurrences of c.
Find the maximum number of substrings that meet the above conditions. If there are multiple solutions with the same number of substrings, return the one with minimum total length. It can be shown that there exists a unique solution of minimum total length.

Notice that you can return the substrings in any order.

 

Example 1:

Input: s = "adefaddaccc"
Output: ["e","f","ccc"]
Explanation: The following are all the possible substrings that meet the conditions:
[
  "adefaddaccc"
  "adefadda",
  "ef",
  "e",
  "f",
  "ccc",
]
If we choose the first string, we cannot choose anything else and we'd get only 1. If we choose "adefadda", we are left with "ccc" which is the only one that doesn't overlap, thus obtaining 2 substrings. Notice also, that it's not optimal to choose "ef" since it can be split into two. Therefore, the optimal way is to choose ["e","f","ccc"] which gives us 3 substrings. No other solution of the same number of substrings exist.
Example 2:

Input: s = "abbaccd"
Output: ["d","bb","cc"]
Explanation: Notice that while the set of substrings ["d","abba","cc"] also has length 3, it's considered incorrect since it has larger total length.
 

Constraints:

1 <= s.length <= 105
s contains only lowercase English letters.




class Solution:
    def maxNumOfSubstrings(self, S: str) -> List[str]:
        mins = [float('inf')] * 26
        maxs = [-1] * 26
        exists = [False] * 26
        prefixSum = [[0]*26 for _ in range(len(S)+1)]
        for i in range(len(S)):
            prefixSum[i+1] = prefixSum[i][:]
            prefixSum[i+1][ord(S[i]) - ord('a')] += 1
            mins[ord(S[i]) - ord('a')] = min(mins[ord(S[i]) - ord('a')], i)
            maxs[ord(S[i]) - ord('a')] = max(maxs[ord(S[i]) - ord('a')], i)
            exists[ord(S[i]) - ord('a')] = True
        graph = [[False]*26 for _ in range(26)]
        for i in range(26):
            if exists[i]:
                for j in range(26):
                    if prefixSum[maxs[i]+1][j] - prefixSum[mins[i]][j] > 0:
                        graph[i][j] = True
        stack = []
        visited = [False] * 26
        for i in range(26):
            if exists[i] and not visited[i]:
                self.dfs(i, graph, stack, visited)
        batch = 0
        batches = [-1] * 26
        degree = [0] * 26
        while stack:
            v = stack.pop()
            if batches[v] < 0:
                self.dfs2(v, graph, batches, batch, degree)
                batch += 1
        res = []
        for i in range(batch-1, -1, -1):
            if degree[i] == 0:
                min_val, max_val = float('inf'), -1
                for j in range(26):
                    if batches[j] == i:
                        min_val = min(mins[j], min_val)
                        max_val = max(maxs[j], max_val)
                res.append(S[min_val:max_val+1])
        return res

    def dfs(self, v, graph, stack, visited):
        if not visited[v]:
            visited[v] = True
            for i in range(26):
                if graph[v][i] and not visited[i]:
                    self.dfs(i, graph, stack, visited)
            stack.append(v)

    def dfs2(self, v, graph, batches, batch, degree):
        if batches[v] < 0:
            batches[v] = batch
            for i in range(26):
                if graph[i][v]:
                    self.dfs2(i, graph, batches, batch, degree)
        else:
            if batches[v] != batch:
                degree[batches[v]] += 1
