Given a m x n matrix mat and an integer threshold, return the maximum side-length of a square with a sum less than or equal to threshold or return 0 if there is no such square.

 

Example 1:


Input: mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], threshold = 4
Output: 2
Explanation: The maximum side length of square with sum less than 4 is 2 as shown.
Example 2:

Input: mat = [[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]], threshold = 1
Output: 0
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 300
0 <= mat[i][j] <= 104
0 <= threshold <= 105




class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])
        prefix = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                prefix[i + 1][j + 1] = mat[i][j] + prefix[i + 1][j] + prefix[i][j + 1] - prefix[i][j]
        
        def check(mid):
            for i in range(m - mid + 1):
                for j in range(n - mid + 1):
                    if prefix[i + mid][j + mid] - prefix[i + mid][j] - prefix[i][j + mid] + prefix[i][j] <= threshold:
                        return True
            return False
        
        left, right = 0, min(m, n) + 1
        while left < right:
            mid = left + (right - left) // 2
            if check(mid):
                left = mid + 1
            else:
                right = mid
        return left - 1
