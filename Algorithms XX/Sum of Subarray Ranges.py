You are given an integer array nums. The range of a subarray of nums is the difference between the largest and smallest element in the subarray.

Return the sum of all subarray ranges of nums.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,2,3]
Output: 4
Explanation: The 6 subarrays of nums are the following:
[1], range = largest - smallest = 1 - 1 = 0 
[2], range = 2 - 2 = 0
[3], range = 3 - 3 = 0
[1,2], range = 2 - 1 = 1
[2,3], range = 3 - 2 = 1
[1,2,3], range = 3 - 1 = 2
So the sum of all ranges is 0 + 0 + 0 + 1 + 1 + 2 = 4.
Example 2:

Input: nums = [1,3,3]
Output: 4
Explanation: The 6 subarrays of nums are the following:
[1], range = largest - smallest = 1 - 1 = 0
[3], range = 3 - 3 = 0
[3], range = 3 - 3 = 0
[1,3], range = 3 - 1 = 2
[3,3], range = 3 - 3 = 0
[1,3,3], range = 3 - 1 = 2
So the sum of all ranges is 0 + 0 + 0 + 2 + 0 + 2 = 4.
Example 3:

Input: nums = [4,-2,-3,4,1]
Output: 59
Explanation: The sum of all subarray ranges of nums is 59.
 

Constraints:

1 <= nums.length <= 1000
-109 <= nums[i] <= 109





class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        from typing import List


        n = len(nums)
        
        # Initialize arrays for previous and next greater/smaller elements
        prev_greater = [0] * n
        next_greater = [0] * n
        prev_smaller = [0] * n
        next_smaller = [0] * n
        
        # Finding previous and next greater elements
        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] < nums[i]:
                next_greater[stack.pop()] = i
            stack.append(i)
        while stack:
            next_greater[stack.pop()] = n
        
        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[i]:
                prev_greater[stack.pop()] = i
            stack.append(i)
        while stack:
            prev_greater[stack.pop()] = -1
        
        # Finding previous and next smaller elements
        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] > nums[i]:
                next_smaller[stack.pop()] = i
            stack.append(i)
        while stack:
            next_smaller[stack.pop()] = n
        
        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] >= nums[i]:
                prev_smaller[stack.pop()] = i
            stack.append(i)
        while stack:
            prev_smaller[stack.pop()] = -1
        
        # Calculate the total range sum
        total_range_sum = 0
        
        for i in range(n):
            max_contribution = (i - prev_greater[i]) * (next_greater[i] - i) * nums[i]
            min_contribution = (i - prev_smaller[i]) * (next_smaller[i] - i) * nums[i]
            total_range_sum += max_contribution - min_contribution
        
        return total_range_sum