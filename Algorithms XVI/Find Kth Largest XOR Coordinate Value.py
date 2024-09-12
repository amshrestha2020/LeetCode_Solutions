You are given a 2D matrix of size m x n, consisting of non-negative integers. You are also given an integer k.

The value of coordinate (a, b) of the matrix is the XOR of all matrix[i][j] where 0 <= i <= a < m and 0 <= j <= b < n (0-indexed).

Find the kth largest value (1-indexed) of all the coordinates of matrix.

 

Example 1:

Input: matrix = [[5,2],[1,6]], k = 1
Output: 7
Explanation: The value of coordinate (0,1) is 5 XOR 2 = 7, which is the largest value.
Example 2:

Input: matrix = [[5,2],[1,6]], k = 2
Output: 5
Explanation: The value of coordinate (0,0) is 5 = 5, which is the 2nd largest value.
Example 3:

Input: matrix = [[5,2],[1,6]], k = 3
Output: 4
Explanation: The value of coordinate (1,0) is 5 XOR 1 = 4, which is the 3rd largest value.
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 1000
0 <= matrix[i][j] <= 106
1 <= k <= m * n





class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        from typing import List
        import heapq

        n, m = len(matrix), len(matrix[0])
        min_heap = []
        
        # Step 1: Compute prefix XOR for each row
        for i in range(n):
            for j in range(1, m):
                matrix[i][j] ^= matrix[i][j - 1]
        
        # Step 2: Compute prefix XOR for each column
        for i in range(m):
            for j in range(1, n):
                matrix[j][i] ^= matrix[j - 1][i]
        
        # Step 3: Use a min-heap to keep track of the k largest values
        for i in range(n):
            for j in range(m):
                if len(min_heap) < k:
                    heapq.heappush(min_heap, matrix[i][j])
                else:
                    if matrix[i][j] > min_heap[0]:
                        heapq.heapreplace(min_heap, matrix[i][j])
        
        return min_heap[0]