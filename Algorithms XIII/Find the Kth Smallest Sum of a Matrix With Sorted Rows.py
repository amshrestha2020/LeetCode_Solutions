You are given an m x n matrix mat that has its rows sorted in non-decreasing order and an integer k.

You are allowed to choose exactly one element from each row to form an array.

Return the kth smallest array sum among all possible arrays.

 

Example 1:

Input: mat = [[1,3,11],[2,4,6]], k = 5
Output: 7
Explanation: Choosing one element from each row, the first k smallest sum are:
[1,2], [1,4], [3,2], [3,4], [1,6]. Where the 5th sum is 7.
Example 2:

Input: mat = [[1,3,11],[2,4,6]], k = 9
Output: 17
Example 3:

Input: mat = [[1,10,10],[1,4,5],[2,3,6]], k = 7
Output: 9
Explanation: Choosing one element from each row, the first k smallest sum are:
[1,1,2], [1,1,3], [1,4,2], [1,4,3], [1,1,6], [1,5,2], [1,5,3]. Where the 7th sum is 9.  
 

Constraints:

m == mat.length
n == mat.length[i]
1 <= m, n <= 40
1 <= mat[i][j] <= 5000
1 <= k <= min(200, nm)
mat[i] is a non-decreasing array.




from typing import List
import heapq

class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        m, n = len(mat), len(mat[0])
        h = [(sum(row[0] for row in mat), [0]*m)]
        seen = set()
        while k > 0:
            sum_, indices = heapq.heappop(h)
            k -= 1
            for i in range(m):
                if indices[i] + 1 < n:
                    new_indices = list(indices)
                    new_indices[i] += 1
                    new_sum = sum_ - mat[i][indices[i]] + mat[i][new_indices[i]]
                    state = tuple(new_indices)
                    if state not in seen:
                        seen.add(state)
                        heapq.heappush(h, (new_sum, new_indices))
        return sum_

