Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr. Since the answer may be large, return the answer modulo 109 + 7.

 

Example 1:

Input: arr = [3,1,2,4]
Output: 17
Explanation: 
Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
Sum is 17.
Example 2:

Input: arr = [11,81,94,43,3]
Output: 444
 

Constraints:

1 <= arr.length <= 3 * 104
1 <= arr[i] <= 3 * 104





class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        stack = []
        prev = [None] * len(arr)
        for i in range(len(arr)):
            while stack and arr[i] <= arr[stack[-1]]:
                stack.pop()
            prev[i] = stack[-1] if stack else -1
            stack.append(i)
        next_ = [None] * len(arr)
        stack = []
        for k in range(len(arr) - 1, -1, -1):
            while stack and arr[k] < arr[stack[-1]]:
                stack.pop()
            next_[k] = stack[-1] if stack else len(arr)
            stack.append(k)
        return sum((i - prev[i]) * (next_[i] - i) * arr[i] for i in range(len(arr))) % MOD
