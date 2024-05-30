Given an integer array arr and an integer k, modify the array by repeating it k times.

For example, if arr = [1, 2] and k = 3 then the modified array will be [1, 2, 1, 2, 1, 2].

Return the maximum sub-array sum in the modified array. Note that the length of the sub-array can be 0 and its sum in that case is 0.

As the answer can be very large, return the answer modulo 109 + 7.

 

Example 1:

Input: arr = [1,2], k = 3
Output: 9
Example 2:

Input: arr = [1,-2,1], k = 5
Output: 2
Example 3:

Input: arr = [-1,-2], k = 7
Output: 0
 

Constraints:

1 <= arr.length <= 105
1 <= k <= 105
-104 <= arr[i] <= 104




class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        MOD = 10**9 + 7
        n = len(arr)
        prefix_sum = suffix_sum = max_subarray_sum = curr_sum = 0
        max_prefix_sum = max_suffix_sum = float('-inf')
        
        for i in range(n):
            prefix_sum += arr[i]
            max_prefix_sum = max(max_prefix_sum, prefix_sum)
        
        for i in range(n-1, -1, -1):
            suffix_sum += arr[i]
            max_suffix_sum = max(max_suffix_sum, suffix_sum)
        
        for i in range(n):
            curr_sum = max(arr[i], curr_sum + arr[i])
            max_subarray_sum = max(max_subarray_sum, curr_sum)
        
        if k == 1:
            return max(0, max_subarray_sum) % MOD
        else:
            return max(0, max_subarray_sum, max_prefix_sum + max_suffix_sum + max(0, sum(arr) * (k-2))) % MOD
