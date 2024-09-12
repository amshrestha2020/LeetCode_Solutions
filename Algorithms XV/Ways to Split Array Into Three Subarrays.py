A split of an integer array is good if:

The array is split into three non-empty contiguous subarrays - named left, mid, right respectively from left to right.
The sum of the elements in left is less than or equal to the sum of the elements in mid, and the sum of the elements in mid is less than or equal to the sum of the elements in right.
Given nums, an array of non-negative integers, return the number of good ways to split nums. As the number may be too large, return it modulo 109 + 7.

 

Example 1:

Input: nums = [1,1,1]
Output: 1
Explanation: The only good way to split nums is [1] [1] [1].
Example 2:

Input: nums = [1,2,2,2,5,0]
Output: 3
Explanation: There are three good ways of splitting nums:
[1] [2] [2,2,5,0]
[1] [2,2] [2,5,0]
[1,2] [2,2] [5,0]
Example 3:

Input: nums = [3,2,1]
Output: 0
Explanation: There is no good way to split nums.
 

Constraints:

3 <= nums.length <= 105
0 <= nums[i] <= 104



class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        MOD = int(1e9 + 7)
        N = len(nums)
        
        # Compute prefix sum array
        A = [0] * N
        A[0] = nums[0]
        for i in range(1, N):
            A[i] = A[i - 1] + nums[i]
        
        def helper(A, left_sum, index, search_left):
            l, r = index, N - 2
            res = -1
            
            while l <= r:
                m = (r - l) // 2 + l
                mid_sum = A[m] - A[index - 1]
                right_sum = A[N - 1] - A[m]
                
                if left_sum <= mid_sum <= right_sum:
                    res = m
                    if search_left:
                        r = m - 1
                    else:
                        l = m + 1
                elif left_sum > mid_sum:
                    l = m + 1
                else:
                    r = m - 1
            
            return res
        
        res = 0
        for i in range(1, N - 1):
            if A[i - 1] > (A[N - 1] - A[i - 1]) // 2:
                break  # early termination
            
            left = helper(A, A[i - 1], i, True)
            right = helper(A, A[i - 1], i, False)
            
            if left == -1 or right == -1:
                continue  # none is satisfied
            
            res = (res + (right - left + 1)) % MOD
        
        return res        